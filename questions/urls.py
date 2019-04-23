from django.conf.urls import url

from questions.views import questions_detail, QuestionList, questions_form

urlpatterns = [
    url(r'^$', QuestionList.as_view(), name='questions_list'),
    url(r'^(?P<question_id>[0-9]+)/$', questions_detail, name='questions_detail'),
    url(r'^form/$', questions_form, name='questions_form'),

]
