from django.contrib import admin

from questions.models import Question, User, Tag

admin.site.register(Question)
admin.site.register(User)
admin.site.register(Tag)
