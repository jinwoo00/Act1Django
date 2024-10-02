from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='course_index'),
    path('details/', views.details, name='course_details'),
    path('enroll/', views.enroll, name='course_enroll'),
]
