"""stepik_job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from vacancies.views import MainView, VacanciesView, CategoryVacanciesView, CompaniesView, VacanciesViewAll, \
    RegisterView, LoginView, VacancySendView, MyCompanyView, MyCompanyVacanciesView, MyCompanyVacancyView, LogoutView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
    path('vacancies/', VacanciesViewAll.as_view()),
    path('vacancies/<int:id>', VacanciesView.as_view()),
    path('vacancies/<int:id>/send', VacancySendView.as_view()),
    path('vacancies/cat/<str:category>', CategoryVacanciesView.as_view()),
    path('companies/<int:id>', CompaniesView.as_view()),
    path('mycompany', MyCompanyView.as_view()),
    path('mycompany/vacancies', MyCompanyVacanciesView.as_view()),
    path('mycompany/vacancies/<int:id>', MyCompanyVacancyView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('register/', RegisterView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
