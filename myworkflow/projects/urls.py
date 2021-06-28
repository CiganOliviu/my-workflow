from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('restapi/development-stack/', views.DevelopmentStackLister.as_view(),
         name='DevelopmentStackLister'),
    path('restapi/development-stack/<int:pk>', views.DevelopmentStackDetails.as_view(),
         name='DevelopmentStackDetails'),
    path('restapi/personal-projects/', views.PersonalProjectsLister.as_view(),
         name='PersonalProjectsLister'),
    path('restapi/personal-projects/<int:pk>', views.PersonalProjectsDetails.as_view(),
         name='PersonalProjectsDetails'),
    path('restapi/organizations/', views.OrganizationsLister.as_view(),
         name='CurrentReadingBooksLister'),
    path('restapi/organizations/<int:pk>', views.OrganizationsDetails.as_view(),
         name='CurrentReadingBooksDetails'),
]
