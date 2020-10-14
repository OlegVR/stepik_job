from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from vacancies.models import Company


class UserRegistrationForm(forms.Form):
    login = forms.CharField(min_length=3, max_length=30, label= 'Логин')
    name = forms.CharField(min_length=2, max_length=40, label='Имя')
    surname = forms.CharField(min_length=2, max_length=40, label='Фамилия')
    password = forms.CharField(min_length=4, max_length=30, label='Пароль')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Зарегистрироваться'))


class UserLogInForm(forms.Form):
    login = forms.CharField(min_length=3, max_length=30, label='Логин')
    password = forms.CharField(min_length=4, max_length=30, label='Пароль')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Войти'))


class UserCompanyForm(forms.ModelForm):
    class Meta:
        model = Company

        fields = (
            'name',
            'location',
            'logo',
            'description',
            'employee_count'
        )
