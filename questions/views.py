# coding=utf-8
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

from questions.models import Question


def questions_list(request):
    contact_list = Question.objects.filter(is_active=True)
    paginator = Paginator(contact_list, 2)  # По 2 на страницу

    page = request.GET.get('page')
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        # В случае, GET параметр не число
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)

    return render(request, 'questions_list.html', {'questions': questions})


def questions_detail(request, question_id):
    return render(request, 'questions_detail.html', {'question': get_object_or_404(Question, pk=question_id)})
