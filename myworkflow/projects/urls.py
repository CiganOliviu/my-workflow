from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('restapi/development-stack/', views.DevelopmentStackLister.as_view(), name='DevelopmentStackLister'),
    path('restapi/development-stack/<int:pk>', views.DevelopmentStackDetails.as_view(), name='DevelopmentStackDetails'),
    path('restapi/personal-projects/', views.PersonalProjectsLister.as_view(), name='DevelopmentStackLister'),
    path('restapi/personal-projects/<int:pk>', views.PersonalProjectsDetails.as_view(), name='DevelopmentStackDetails'),
    path('restapi/personal-finished-projects/', views.PersonalFinishedProjectLister.as_view(), name='PersonalFinishedProjectLister'),
    path('restapi/university-projects/', views.UniversityProjectLister.as_view(), name='DevelopmentStackLister'),
    path('restapi/university-projects/<int:pk>', views.UniversityProjectsDetails.as_view(), name='DevelopmentStackDetails'),
]
