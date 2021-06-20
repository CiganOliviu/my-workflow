from django.contrib import admin
from .models import *


class PersonalProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'stack', 'start_date', 'importance_level', 'project_visibility')


class PersonalFinishedProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'stack')


class UniversityProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'deadline')


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'gmail', 'url')


admin.site.register(DevelopmentStack)
admin.site.register(PersonalProject, PersonalProjectAdmin)
admin.site.register(UniversityProject, UniversityProjectAdmin)
admin.site.register(UniversityClasses)
admin.site.register(Organization, OrganizationAdmin)

admin.site.site_header = "MyWorkflow"
