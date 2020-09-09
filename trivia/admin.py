from django.contrib import admin

from trivia.models import Question, Attempt, Limit


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'closed_at', 'event', 'team_a', 'team_b', 'status')
    list_filter = ('status',)
    ordering = ('closed_at', 'status',)


class AttemptAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'status')
    list_filter = ('status',)
    ordering = ('status',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Attempt, AttemptAdmin)
admin.site.register(Limit)
