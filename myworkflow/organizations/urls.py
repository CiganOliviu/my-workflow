from django.urls import path
from . import views

urlpatterns = [

    path('restapi/organizations/', views.OrganizationsLister.as_view(),
         name='CurrentReadingBooksLister'),
    path('restapi/organizations/<int:pk>', views.OrganizationsDetails.as_view(),
         name='CurrentReadingBooksDetails'),
]
