from django.db import models
from users.models import User



class BioData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    discovery = models.CharField(max_length=30, null=True)
    age = models.CharField(max_length=30, null=True)
    attempted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Question(models.Model):
    text = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.text

class SelfQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.CharField(max_length=300, null=True)
    time = models.DateTimeField(auto_now_add=True, null=True)
    def __str__(self):
        return '{} - {}'.format(self.question, self.pk)
        # return self.question.text