# coding=utf-8
from random import randint

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from questions.forms import QuestionForm
from questions.models import Question


class QuestionList(ListView):
    model = Question
    paginate_by = 10


def questions_detail(request, question_id):
    return render(request, 'questions_detail.html', {'question': get_object_or_404(Question, pk=question_id)})


def ajax_count(request):
    return JsonResponse(
        {'tags': [t.title for t in Question.objects.get(id=request.POST['item_id']).tags.all()]}
    )

def questions_form(request):
    # if this is a POST request we need to process the form data

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = QuestionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            return redirect('questions_list')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = QuestionForm()

    return render(request, 'questions_form.html', {'form': form})
