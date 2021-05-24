from django.contrib import admin
from .models import *

admin.site.register(DevelopmentStack)
admin.site.register(PersonalProjects)
admin.site.register(UniversityProjects)

admin.site.site_header = "MyWorkflow"