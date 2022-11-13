from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
   path('questions/', views.question_list, name='question_list'),
]
urlpatterns = [
   path('', views.question_list, name='question_list'),
   path('<int:question_id>/', views.question_detail, name='question_detail'),
   path('add/', view=views.question_add, name="question-add"),
   path('add-choice/', view=views.choice_add, name='choice-add')
]