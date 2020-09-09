from django.contrib import messages
from django.db.models import F
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, reverse, get_object_or_404
from django.utils import timezone, dateparse
from datetime import date
from django.views import View
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import Wallet
from stack.models import Team
from trivia.forms import QuestionForm, ResultQuestionForm
from trivia.helpers.marking import Marking
from trivia.models import Question, Attempt, Limit


def index_view(request):
    questions = Question.objects.filter(status='open', closed_at__gt=timezone.now())
    num_entries = 0
    if request.user.is_authenticated:
        num_entries = Attempt.objects.filter(user=request.user.pk, question__status='open').count()
    return render(request, 'trivia/index.html', {'questions': questions, 'num_entries': num_entries})


class AdminTrivia(View):
    form = QuestionForm

    def get(self, request):
        questions = Question.objects.filter()
        teams = Team.objects.all().order_by('-id')
        return render(request, 'trivia/admin/index.html', {'questions': questions, 'form': self.form, 'teams': teams})

    # def post(self, request):
    #     form = self.form(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, 'Question Added Successfully.')
    #         return HttpResponseRedirect(reverse('myadmin:trivia'))
    #
    #     questions = Question.objects.filter()
    #     teams = Team.objects.all().order_by('-id')
    #     return render(request, 'trivia/admin/index.html', {'questions': questions, 'form': form, 'teams': teams})


def cancel_question(request, pk):
    if request.method == 'POST':
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

        if not question.status == 'open':
            messages.warning(request, 'Question cannot be closed as status is not open.')
            return HttpResponseRedirect(reverse('myadmin:trivia'))

        # THIS CODE IS TO RETURN THE N20 STAKE USERS WILL USE TO PLAY THE TRIVIA
        # if question.num_players > 0:
        #     attempts = Attempt.objects.filter(question=question.pk)

        #     for attempt in attempts:
        #         user_wallet = Wallet.objects.get(user=attempt.user.pk)
        #         user_wallet.balance = F('balance') + 20
        #         user_wallet.save(update_fields=('balance',))

        question.status = 'canceled'
        question.save(update_fields=('status',))

        messages.warning(request, 'Question canceled.')
        return HttpResponseRedirect(reverse('myadmin:trivia'))

    raise Http404

#VIEW FOR ADMIN TO RESULT A GAME
class AdminTriviaResult(View):
    form = ResultQuestionForm

    def get(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

        return render(request, 'trivia/admin/edit.html', {'question': question, 'form': self.form})

    def post(self, request, pk):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

        if not question.status == 'open':
            messages.warning(request, 'Question cannot be resulted as status is not open.')
            return HttpResponseRedirect(reverse('myadmin:trivia_result', args=[pk]))

        form = self.form(request.POST, instance=question)

        if form.is_valid():
            question_instance = form.save()
            Marking(question_instance)
            messages.success(request, 'Question Resulted Successfully.')
            return HttpResponseRedirect(reverse('myadmin:trivia'))

        return render(request, 'trivia/admin/edit.html', {'question': question, 'form': self.form})

#VIEW FOR USERS THAT WANT TO ATTEMPT A TRIVIA QUESTION
class QuestionView(View):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)

        #INCREMENTING THE PLAY BUTTON
        today = date.today()
        try:
            attempt = Attempt.objects.filter(user=request.user, day_created=today)
            attempt_count = 4 - attempt.count()
        except Attempt.DoesNotExist:
            attempt_count = 4

        if question.closed_at <= timezone.now():
            messages.warning(request, 'Match is closed for entry.')
            return HttpResponseRedirect(reverse('trivia:index'))

        return render(request, 'trivia/details.html', {'question': question, 'attempt_count':attempt_count})

    def post(self, request, pk):
        #team_a_score = request.POST.get('team_a_score')
        total_score = request.POST.get('total_score')
        penalty = request.POST.get('penalty')
        total_cards = request.POST.get('total_cards')

        try:
            limit = Limit.objects.get(user=request.user)
        except Limit.DoesNotExist:
            limit = False

        # if not team_a_score or not team_b_score or not total_corner_kicks or \
        #         not total_cards:
        #     messages.warning(request, 'Please fill in all fields.')
        #     return HttpResponseRedirect(reverse('trivia:question', args=[pk]))

        if not total_score or not penalty or \
                not total_cards:
            messages.warning(request, 'Please fill in all fields.')
            return HttpResponseRedirect(reverse('trivia:question', args=[pk]))

        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

        if limit:
            messages.warning(request, 'You have exceeded your daily attempt')
            return HttpResponseRedirect(reverse('trivia:question', args=[pk]))

        if question.closed_at <= timezone.now():
            messages.warning(request, 'Match is closed for entry.')
            return HttpResponseRedirect(reverse('trivia:index'))

        # wallet = Wallet.objects.get(user=request.user.pk)

        # if wallet.balance < 20:
        #     messages.warning(request, 'Your balance is not enough. Please topup and try again.')
        #     return HttpResponseRedirect(reverse('trivia:question', args=[pk]))

        # wallet.balance = F('balance') - 20
        # wallet.save(update_fields=('balance',))

        #MY WORK AROUND TO GET THE VALUE FOR PENALTY FROM THE FRONTEND
        if penalty == 'YES':
            penalty_val = True
        elif penalty == 'NO':
            penalty_val = False
  

        Attempt.objects.create(user=request.user, question=question, total_score=total_score,
                               penaltya=penalty_val, total_cards=total_cards)
        today = date.today()
        print('today:',today)
        attempt = Attempt.objects.filter(user=request.user, day_created=today)
        if attempt.count() >=4:
            Limit.objects.create(user=request.user)
        
        messages.success(request, 'Entry submitted Successfully.')
        return HttpResponseRedirect(reverse('trivia:index'))

#creating a trivia question
class SetQuestionView(View):
    permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        return render(request, 'trivia/admin/question.html')

    def post(self, request):
        closed_at = request.POST.get('closed_at')
        print(closed_at)
        # dateparse.parse_datetime(closed_at)
        # print('1', closed_at)
        # print(closed_at)
        event = request.POST.get('event')
        print(event)
        team_a = request.POST.get('team_a')
        print(team_a)
        team_b = request.POST.get('team_b')
        print(team_b)
        team_a_logo = request.FILES.get('team_a_logo')
        print(team_a_logo)
        print(type(team_a_logo))
        team_b_logo = request.FILES.get('team_b_logo')
        print(team_b_logo)

        if not closed_at or not event or not team_a or not team_b or not team_a_logo or not team_b_logo:
            messages.error(request, 'Please fill all the fields')
            return HttpResponseRedirect(reverse('myadmin:trivia_question'))
        
        Question.objects.create(closed_at=closed_at, event=event, team_a=team_a, team_b=team_b, team_a_logo=team_a_logo, team_b_logo=team_b_logo,
                                )
        messages.success(request, "trivia game has been created successfully")
        return HttpResponseRedirect(reverse('myadmin:trivia'))


def entries_view(request):
    entries = Attempt.objects.filter(user=request.user.pk)
    return render(request, 'trivia/entries.html', {'entries': entries})


def entry_view(request, pk):
    try:
        entry = Attempt.objects.get(pk=pk)
        #MY QUICKFIX TO DISPLAY THE PENALTY VALUE ON THE ENTRY PAGE
        if entry.penaltya == True:
            pen_entry = "YES"
        elif entry.penaltya == False:
            pen_entry ='NO'

        if entry.question.penalty == True:
            ques_pen = 'Yes'
        elif entry.question.penalty == False:
            ques_pen = 'No'

    except Attempt.DoesNotExist:
        raise Http404

    context = {
        'entry': entry,
        'pen_entry':pen_entry,
        'ques_pen':ques_pen
    }

    return render(request, 'trivia/entry.html', context)
