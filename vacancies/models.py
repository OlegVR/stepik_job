from django.db import models
from django.contrib.auth.models import User

from stepik_job.settings import MEDIA_COMPANY_IMAGE_DIR, MEDIA_SPECIALITY_IMAGE_DIR


class Company(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=70, blank=True, null=True)
    logo = models.ImageField(upload_to=MEDIA_COMPANY_IMAGE_DIR, blank=True, null=True)
    description = models.CharField(max_length=455, blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)


class Specialty(models.Model):
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=120)
    picture = models.ImageField(upload_to=MEDIA_SPECIALITY_IMAGE_DIR)


class Vacancy(models.Model):
    title = models.CharField(max_length=90)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancies')
    skills = models.CharField(max_length=180)
    description = models.CharField(max_length=250)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()


class Application(models.Model):
    written_username = models.CharField(max_length=30)
    written_phone = models.IntegerField()
    written_cover_letter = models.CharField(max_length=570)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
