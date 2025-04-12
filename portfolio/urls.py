from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_view, name='projects'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success_view, name='contact_success'),
]
