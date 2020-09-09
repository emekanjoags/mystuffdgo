from django.shortcuts import render
from rest_framework import permissions, status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User
from .serializers import BioDataSerializer
from .models import BioData, Question, SelfQuestion
from django.utils.decorators import decorator_from_middleware
from admin.middleware import  AdminCheckMiddleware

class BioDataDisplay(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        try:
            queryset = BioData.objects.get(user=request.user)
        except BioData.DoesNotExist:
            return Response(data={'response':'false'}, status=status.HTTP_200_OK)
        serializer = BioDataSerializer(queryset, many=True)
        return Response(data={'response':'true'}, status=status.HTTP_200_OK )

    def post(self, request):
        data = request.data

        gender = data.get('gender')
        age = data.get('age')
        country = data.get('country')
        state = data.get('state')
        discovery = data.get('discovery')
        BioData.objects.create(user=request.user, gender=gender, age=age, country=country, state=state, discovery=discovery)
        return Response(data=
        {'response':'Thank you for participating in this survey, this will greatly improve our service to you! Click the withdraw button to finish'},
         status=status.HTTP_200_OK)

@decorator_from_middleware(AdminCheckMiddleware)
def adminSurvey(request):
    questions = Question.objects.all()
    return render(request, 'site_admin/survey/index.html', {'questions':questions})
    
@decorator_from_middleware(AdminCheckMiddleware)
def bio_data(request):
    biodata = BioData.objects.all()
    return render(request, 'site_admin/survey/biodata.html', {'biodata':biodata})



class QuestionDisplay(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    
    def get(self, request):
        try:
            question_queryset = Question.objects.all()
        except Question.DoesNotExist:
            return Response(data={'response': 'true'}, status=status.HTTP_200_OK)
        try:
            answered_queryset = SelfQuestion.objects.filter(user=request.user)
        except SelfQuestion.DoesNotExist:
            return Response(data={'response': 'true'}, status=status.HTTP_200_OK)  
        
        questions=[]
        answered_questions = []
        for answer in answered_queryset:
            answered_questions.append(answer.question.text)
        count = question_queryset.count()
        for i in range(count):
            if question_queryset[i].text in answered_questions:
                continue
            questions.append(question_queryset[i].text)
        if questions == []:
            return Response(data={'response': 'true'}, status=status.HTTP_200_OK) 
        question = questions[0]
        return Response(data={'question':question, 'response':'false'}, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            question_queryset = Question.objects.all()
        except Question.DoesNotExist:
            return Response(data={'response':'somethin went wrong, please contact our suport team'}, status=status.HTTP_400_BAD_REQUEST)
        data = request.data
        answer = data.get('answer')
        question = data.get('question')

        count = question_queryset.count()
        for i in range(count):
            if question in question_queryset[i].text:
                current_question = question_queryset[i]
                break
        SelfQuestion.objects.create(user=request.user, answer=answer, question=current_question)
        return Response(data={'response':'Thank you for participating in this survey, this will greatly improve our service to you! Click the withdraw button to finish'})

@decorator_from_middleware(AdminCheckMiddleware)
def otherQuestions(request, pk):
        questions = SelfQuestion.objects.filter(question=pk)
        return render(request, 'site_admin/survey/survey-results.html', {'questions':questions})