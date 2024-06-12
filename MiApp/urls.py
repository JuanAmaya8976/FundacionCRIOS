from django.urls import path
from . import views

urlpatterns=[
    path('', views.hola),
    path('restringir/', views.hola2)
]