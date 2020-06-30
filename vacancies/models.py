from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=70)
    logo = models.CharField(max_length=256, default=None)
    description = models.CharField(max_length=455)
    employee_count = models.IntegerField()


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    picture = models.CharField(max_length=455, default=None)


class Vacancy(models.Model):
    title = models.CharField(max_length=90)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=180)
    description = models.CharField(max_length=250)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()