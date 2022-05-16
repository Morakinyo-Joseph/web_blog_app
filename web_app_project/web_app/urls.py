from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logging_out, name='logging_out'),
]
