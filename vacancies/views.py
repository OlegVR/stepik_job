from django.shortcuts import render

from django.views import View
from django.http import Http404
from vacancies.models import Specialty, Vacancy, Company


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


class RegisterView(View):
    def get(self, request):

        return render(request, 'register.html')


class LoginView(View):
    def get(self, request):

        return render(request, 'login.html')


class LogoutView(View):
    def get(self, request):

        return render(request, 'index.html')


class VacancySendView(View):
    def get(self, request, id):

        return render(request, 'sent.html')


class MyCompanyView(View):
    def get(self, request):

        return render(request, 'company-edit.html')


class MyCompanyVacanciesView(View):
    def get(self, request):

        return render(request, 'vacancy-list.html')


class MyCompanyVacancyView(View):
    def get(self, request, id):

        return render(request, 'vacancy-edit.html')
