from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Survey(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class CompletedSurvey(models.Model):
    survey = models.ForeignKey(Survey)
    title = models.CharField(max_length=300)

    def __unicode__(self):
        return self.survey


class Question(models.Model):
    survey = models.ForeignKey(Survey)
    question = models.CharField(max_length=300)

    def __unicode__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question)
    completed_survey = models.ForeignKey(CompletedSurvey)
    answer = models.CharField(max_length=255)

    def __unicode__(self):
        return self.completed_survey




