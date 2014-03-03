from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Survey(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    url = models.SlugField()

    def __unicode__(self):
        return self.name


class Question(models.Model):
    question = models.ForeignKey(Survey)
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User)
    url = models.SlugField()

    def __unicode__(self):
        return self.question

# class Answers(models.Model):
#     answer = models.ForeignKey(Questions)
#
#     def __unicode__(self):
#         return self.answer


