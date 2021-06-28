from django.urls import path
from . import views

urlpatterns = [
    path('restapi/current-reading-books/', views.CurrentReadingBooksLister.as_view(),
         name='CurrentReadingBooksLister'),
    path('restapi/current-reading-books/<int:pk>', views.CurrentReadingBooksDetails.as_view(),
         name='CurrentReadingBooksDetails'),
]