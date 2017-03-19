from django.shortcuts import render

QUESTIONS = {
    '1': {'id': 1, 'title': 'I`m your dream', 'text': 'I`m your dream, make you real'},
    '2': {'id': 2, 'title': 'I`m your eyes', 'text': 'I`m your eyes when you must steal'},
    '3': {'id': 3, 'title': 'I`m your pain', 'text': 'I`m your pain when you can`t feel'},
}


def questions_list(request):
    return render(request, 'questions_list.html', {'questions': QUESTIONS.values()})


def questions_detail(request, question_id):
    return render(request, 'questions_detail.html', {'question': QUESTIONS.get(question_id, {})})
