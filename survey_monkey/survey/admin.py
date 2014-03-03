from django.contrib import admin
from survey.models import Question, Survey


class QuestionInlineAdmin(admin.StackedInline):
    model = Question

class SurveyAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    inlines = [QuestionInlineAdmin]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)