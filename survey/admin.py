from django.contrib import admin

from .models import BioData, Question, SelfQuestion

admin.site.register(BioData)
admin.site.register(Question)
admin.site.register(SelfQuestion)
