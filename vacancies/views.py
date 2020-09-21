from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse

from django.views import View
from django.http import Http404, HttpResponse
from django.views.generic import CreateView

from vacancies.forms import UserRegistrationForm, UserLogInForm
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
#    model = User
#    form_class = UserRegistrationForm
#    success_url = 'login'
#    template_name = 'register.html'

    def get(self, request):
        form = UserRegistrationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            data = register_form.cleaned_data
            user = User.objects.create_user(first_name=data['name'], username=data['login'],
                                            last_name=data['surname'], password=data['password'])
            user.save()
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
                return redirect('/mycompany/')
            else:
                return HttpResponse('Неверный логин или пароль')




class LogoutView(View):

    def get(self, request):

        return render(request, 'index.html')


class VacancySendView(View):

    def get(self, request, id):

        return render(request, 'sent.html')


class MyCompanyView(View):
    ''' Раздел компании Попасть в него можно через выпадающее меню.
        Если у пользователя еще нет компании, ему предлагается создать ее.
        Если  есть – он сразу же переходит к его редактированию!'''

    def get(self, request):

        return render(request, 'company-create.html')


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
