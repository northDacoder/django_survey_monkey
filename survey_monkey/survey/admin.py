from django.contrib import admin
from survey.models import Question, Survey, Answer, CompletedSurvey


class QuestionInlineAdmin(admin.TabularInline):
    model = Question

class AnswerInlineAdmin(admin.TabularInline):
    model = Answer

class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    inlines = [QuestionInlineAdmin]

class CompletedSurveyAdmin(admin.ModelAdmin):
    inlines = [AnswerInlineAdmin]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(CompletedSurvey, CompletedSurveyAdmin)
admin.site.register(Question)
admin.site.register(Answer)