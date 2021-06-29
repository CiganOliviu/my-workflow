from django.contrib import admin
from .models import Organization


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'gmail', 'url')


admin.site.register(Organization, OrganizationAdmin)
