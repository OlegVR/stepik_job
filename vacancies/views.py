from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from django.http import Http404, HttpResponse
from django.views.generic import CreateView

from vacancies.forms import UserRegistrationForm, UserLogInForm, UserCompanyForm
from vacancies.models import Specialty, Vacancy, Company, User


class MainView(View):

    def get(self, request):
        specialty = Specialty.objects.all()
        company = Company.objects.all()
        context = {"specialty": specialty, "company": company}

        return render(request, 'index.html', context=context)


class VacanciesViewAll(View):

    def get(self, request):
        vacancies_all = Vacancy.objects.all()
        context = {'vacancies': vacancies_all}
        return render(request, 'vacancies_all.html', context=context)


class VacanciesView(View):

    def get(self, request, id):
        vacancies= Vacancy.objects.filter(id=id).first()
        if vacancies:
            company = vacancies.company
            logo = company.logo
            context = {'vacancy': vacancies, 'logo': logo}
            return render(request, 'vacancy.html', context=context)

        else:
            raise Http404


class CategoryVacanciesView(View):

    def get(self, request, category):
        speciality= Specialty.objects.filter(code=category).first()

        if speciality:
            vacancies = speciality.vacancies.all()
            context = {'vacancies': vacancies, 'category_name': speciality.title}

            return render(request, 'vacancies.html', context=context)

        else:
            raise Http404


class CompaniesView(View):

    def get(self, request, id):
        company = Company.objects.filter(id=id).first()

        if company:
            vacancies_company = company.vacancies.all()
            context = {'company': company, 'vacancies': vacancies_company}

            return render(request, 'company.html', context=context)

        else:
            raise Http404


class RegisterView(CreateView):

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            User.objects.create_user(first_name=data['name'], username=data['login'],
                                     last_name=data['surname'], password=data['password'])
            return redirect('/')
        else:
            return HttpResponse("Некорректно заполнена форма регистрации")


class MyLoginView(LoginView):

    def get(self, request):
       form = UserLogInForm()
       return render(request, 'login.html', {'form': form})

    def post(self, request):
        login_form = UserLogInForm(request.POST)
        if login_form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                return HttpResponse('<h2>Упс!</h2><p><h4>Неверный логин или пароль</h4></p>')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')


class VacancySendView(View):

    def get(self, request, id):
        return render(request, 'sent.html')


class MyCompanyView(View):
    ''' Раздел компании Попасть в него можно через выпадающее меню.
        Если у пользователя еще нет компании, ему предлагается создать ее.
        Если  есть – он сразу же переходит к его редактированию!'''

    def get(self, request):
        form = UserCompanyForm
        if request.user.is_authenticated:
            username = request.user.username
            user = User.objects.filter(username=username).first()
            user_company = Company.objects.filter(owner=user).first()
            if user_company:
                context = {'user': user, 'user_company': user_company, 'form': form}
                return render(request, 'company-edit.html', context=context)

            return render(request, 'company-create.html')

    def post(self, request):
        form = UserCompanyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            username = request.user.username
            user = User.objects.filter(username=username).first()
            Company.objects.create(
                name=data['name'], location=data['location'],
                logo=data['logo'], description=data['description'],
                empoloyee_count=data['employee_count'], owner=user
            )
            return redirect('mycompany')

        else:

            return HttpResponse('<h3>Вы неправильно заполнили форму. Попробуйте заново.</h3>')


class NonCompanyView(View):
    def get(self, request):
        return render(request, 'company-edit.html')


class MyCompanyVacanciesView(View):

    '''Раздел вакансии
       Из карточки компании через левое меню можно перейти к вакансиям.
       Если у пользователя еще нет вакансий, ему предлагается создать их.
       Если вакансии есть – они выводятся в списке, из которого можно перейти на карточку вакансии'''

    def get(self, request):

        return render(request, 'vacancy-list.html')


class MyCompanyVacancyView(View):
    '''На карточке вакансии можно отредактировать ее.'''

    def get(self, request, id):

        return render(request, 'vacancy-edit.html')
