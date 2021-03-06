from django.urls import path

from questions.views import questions_detail, QuestionList

urlpatterns = [
    path('', QuestionList.as_view(), name='questions_list'),
    path('<int:number>/', questions_detail, name='questions_detail'),
]
