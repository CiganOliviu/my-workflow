from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('development-stack/', views.DevelopmentStackLister.as_view(), name='DevelopmentStackLister'),
    path('authors/<int:pk>', views.DevelopmentStackDetails.as_view(), name='DevelopmentStackDetails'),
]
