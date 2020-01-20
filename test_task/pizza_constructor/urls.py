from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registration/', views.register, name='registration'),
]

