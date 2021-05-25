from django.contrib import admin
from .models import *


class PersonalProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'stack', 'start_date')


class PersonalFinishedProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'stack')


class UniversityProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'deadline')


admin.site.register(DevelopmentStack)
admin.site.register(PersonalProject)
admin.site.register(PersonalFinishedProject)
admin.site.register(UniversityProject)
admin.site.register(UniversityClasses)

admin.site.site_header = "MyWorkflow"
