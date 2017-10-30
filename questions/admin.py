from django.contrib import admin

from questions.models import Question, User

admin.site.register(Question)
admin.site.register(User)
