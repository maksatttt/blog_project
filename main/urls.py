from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('about2/', views.about2, name='about2'),
    path('contacts/', views.contacts_view, name='contacts'),
]