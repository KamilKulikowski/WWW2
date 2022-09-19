from django.contrib import admin
# from polls.models import Question, Choice, Answer
from .models import Question, Choice, Answer
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_filter = ('pub_date',)
    search_fields = ("question_text", )

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', "votes")
    list_filter = ('votes',)
    search_fields = ("question_text",)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')
    # list_filter = ('pub_date',)
    # search_fields = ("question",)




admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Answer, AnswerAdmin)
