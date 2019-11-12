from django.urls import path

from questions.views import questions_detail, QuestionList

urlpatterns = [
    path('', QuestionList.as_view(), name='questions_list'),
    path('<int:question_id>/', questions_detail, name='questions_detail'),
]
