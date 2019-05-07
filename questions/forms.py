from django import forms
from django.core.exceptions import ValidationError

from questions.models import Question, Tag


class QuestionForm(forms.ModelForm):
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    #
    # title = models.CharField(max_length=120, verbose_name=u"Заголовок вопроса")
    # text = models.TextField(verbose_name=u"Полное описание вопроса")
    #
    # create_date = models.DateTimeField(default=datetime.now, verbose_name=u"Время создания вопроса")
    #
    # is_active = models.BooleanField(default=True, verbose_name=u"Доступность вопроса")
    #
    tags = forms.CharField(label='Tags', max_length=120, widget=forms.TextInput(attrs={'size':'40', 'class': 'super'}))

    def clean(self):
        cleaned_data = super(QuestionForm, self).clean()

        data = self.cleaned_data['tags']
        if not data:
            raise forms.ValidationError("You have forgotten about tags!")

        if len(data.split(',')) < 2:
            raise forms.ValidationError("Need more gold!")

        self.cleaned_data['tags'] = [Tag.objects.get_or_create(title=tag)[0].pk for tag in data.split(',')]
        return self.cleaned_data

    # def clean(self):
    #     return {}

    # def save(self, commit=True):
    #     i = self.Meta.model.objects.create(self.instance)
    #     return i

    class Meta:
        model = Question
        fields = ('author', 'title', 'text', 'create_date', 'tags')
