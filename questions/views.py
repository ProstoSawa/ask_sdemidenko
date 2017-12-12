# coding=utf-8
import requests
import json

from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView

from questions.models import Question


class QuestionList(ListView):
    model = Question
    paginate_by = 1


def questions_detail(request, question_id):
    return render(request, 'questions_detail.html', {'question': get_object_or_404(Question, pk=question_id)})


def send_message(request):
    """
    Пример через curl http://controller.sdemidenko.notkube.dev.ivi.ru/publish/id=ch1 -d "Hi, All!"

    Статитистика http://controller.sdemidenko.notkube.dev.ivi.ru/channels-stats
    """

    PUB_URL = 'http://controller.sdemidenko.notkube.dev.ivi.ru/publish/'

    cid = request.GET.get('to')
    text = request.GET.get('text')
    body = json.dumps({'messages': [text]})
    try:
        # TODO: может быть долгим
        resp = requests.post(PUB_URL, params={'id': cid}, data=text)
        if resp.status_code == 200:
            return JsonResponse({"status": "ok", "msg": resp.text})
        else:
            return JsonResponse({"status": "error", "msg": resp.text, "code": resp.status_code})
    except Exception as e:
        return JsonResponse({"status": "exception", "e": e})
