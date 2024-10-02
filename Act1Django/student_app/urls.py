from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='student_index'),
    path('about/', views.about, name='student_about'),
    path('contact/', views.contact, name='student_contact'),
]
