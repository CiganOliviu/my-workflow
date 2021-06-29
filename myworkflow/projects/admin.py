from django.contrib import admin
from .models import *


class PersonalProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'stack', 'start_date', 'importance_level', 'project_visibility')


class CurrentReadingBookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'type', 'read')


class PortfolioProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'stack')


admin.site.register(DevelopmentStack)
admin.site.register(PersonalProject, PersonalProjectAdmin)
admin.site.register(PortfolioProject, PortfolioProjectAdmin)


admin.site.site_header = "My Workflow"
