from django.urls import path
from . import views

urlpatterns=[
    path('', views.gentest),
    path('index/', views.genindex),
]