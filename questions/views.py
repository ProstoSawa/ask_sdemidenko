# coding=utf-8
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView

from questions.forms import QuestionForm
from questions.models import Question


class QuestionList(ListView):
    model = Question
    paginate_by = 1


class QuestionDetail(DetailView):
    model = Question


def questions_detail(request, question_id):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/')
    else:
        form = QuestionForm()

    return render(request, 'questions_detail.html', {
        'question': get_object_or_404(Question, pk=question_id),
        'form': QuestionForm(),
    })
