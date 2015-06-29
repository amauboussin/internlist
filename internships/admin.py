from internships.models import *

from django.contrib import admin


class JobAdmin(admin.ModelAdmin):
    pass

class CompanyAdmin(admin.ModelAdmin):
    pass

admin.site.register(Job, JobAdmin)
admin.site.register(Company, CompanyAdmin)