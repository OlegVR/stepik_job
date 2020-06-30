from data import companies, specialties, jobs
from vacancies.models import Company, Specialty, Vacancy


def load_db():
    for company in companies:
        Company.objects.create(name=company["title"], location=company["location"], description=company["description"],
                               employee_count=company["employee_count"], logo=company["logo"])
    for specialty in specialties:
        Specialty.objects.create(code=specialty["code"], title=specialty["title"], picture=specialty["picture"])

    for vacancy in jobs:
        specialty = Specialty.objects.get(code=vacancy["cat"])

        company = Company.objects.get(name=vacancy["company"])

        Vacancy.objects.create(title=vacancy["title"], specialty=specialty, company=company,
                               skills=vacancy["skills"], description=vacancy["desc"], salary_min=vacancy["salary_from"],
                               salary_max=vacancy["salary_to"], published_at=vacancy["posted"])
