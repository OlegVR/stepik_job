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
        return render(request, 'vacanvies_all.html', context=context)


class VacanciesView(View):
    def get(self, request, id):
        vacancies_all = Vacancy.objects.all()

        if id:
            vacancies = vacancies_all.filter(id=id)

            if len(vacancies) > 0:
                vacancies = vacancies[0]
                company = vacancies.company
                logo = company.logo
                context = {'vacancy': vacancies, 'logo': logo}

                return render(request, 'vacancy.html', context=context)

            else:
                raise Http404

        else:
            context = {'vacancies': vacancies_all}

            return render(request, 'vacancies_all.html', context=context)


class CategoryVacanciesView(View):
    def get(self, request, category):
        vacancies = Vacancy.objects.filter(specialty__code=category)
        cat_vacancies = Specialty.objects.filter(code=category)
        if len(vacancies) > 0 or len(cat_vacancies) > 0:
            context = {'categories': vacancies, 'category_name': cat_vacancies[0].title}

            return render(request, 'vacancies.html', context=context)

        else:
            raise Http404


class CompaniesView(View):
    def get(self, request, id=0):
        companies_all = Company.objects.all()

        if id:
            id_companies = companies_all.filter(id=id)

            if len(id_companies) > 0:
                vacancies_company = Vacancy.objects.filter(company__id=id)
                context = {'company': id_companies[0], 'vacancies': vacancies_company}

                return render(request, 'company.html', context=context)

            else:
                raise Http404

        else:
            raise Http404