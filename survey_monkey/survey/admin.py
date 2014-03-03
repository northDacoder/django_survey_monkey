from django.contrib import admin
from survey_monkey.survey.models import Question, Survey


class QuestionInlineAdmin(admin.StackedInline):
    model = Question

class SurveyAdmin(admin.ModelAdmin):
    list_display = ("id", "posted", "title", "author")
    search_fields = ("title", "author__username")
    readonly_fields = ("author",)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()

admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)