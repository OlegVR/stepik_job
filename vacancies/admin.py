from django.contrib import admin
from .models import Company, Specialty, User



class CompanyAdmin(admin.ModelAdmin):
    pass


class SpecialtyAdmin(admin.ModelAdmin):
    pass


admin.site.register(Company, CompanyAdmin)
admin.site.register(Specialty, SpecialtyAdmin)
