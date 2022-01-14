from django.forms import Form, CharField, BooleanField, ModelChoiceField, ModelForm, TextInput, Textarea, Select, \
    CheckboxInput, ValidationError
from .models import News, Category
import re


class NewsForm(Form):
    title = CharField(max_length=150, label='Название', widget=TextInput(attrs={"class": "form-control"}))
    content = CharField(label='Текст', widget=Textarea(attrs={"class": "form-control", "rows": "5"}))
    is_published = BooleanField(label='Опубликовать?', initial=True,
                                widget=CheckboxInput(attrs={"class": "form-check-input"}))
    category = ModelChoiceField(queryset=Category.objects.all(), label='Категория', empty_label='',
                                widget=Select(attrs={"class": "form-select"}))


class NewsForm2(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': TextInput(attrs={"class": "form-control"}),
            'content': Textarea(attrs={"class": "form-control", "rows": "5"}),
            'is_published': CheckboxInput(attrs={"class": "form-check-input"}),
            'category': Select(attrs={"class": "form-control"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if re.match(r'\d', title):
            raise ValidationError('Название не должно начинаться с цифры')
        return title
