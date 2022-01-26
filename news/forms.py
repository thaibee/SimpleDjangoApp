from django.forms import Form, CharField, BooleanField, ModelChoiceField, ModelForm, TextInput, Textarea, Select, \
    CheckboxInput, ValidationError, EmailInput, PasswordInput
from .models import News, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class UserRegistrationForm(UserCreationForm):
    username = CharField(max_length=150, label='Имя пользователя', widget=TextInput(attrs={"class": "form-control"}))
    email = CharField(max_length=150, label='E-Mail', widget=EmailInput(attrs={"class": "form-control"}))
    password1 = CharField(label='Пароль', widget=PasswordInput(attrs={"class": "form-control"}))
    password2 = CharField(label='Подтверждение пароля', widget=PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


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
