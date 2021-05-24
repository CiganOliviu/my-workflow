from django.contrib import admin
from .models import *

admin.site.register(DevelopmentStack)
admin.site.register(PersonalProject)
admin.site.register(UniversityProject)

admin.site.site_header = "MyWorkflow"