from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('register/', views.register, name='register'),
    path('logging_in', views.logging_in, name='logging_in'),
    path('logging_out', views.logging_out, name='logging_out'),
    path('post/<str:pk>', views.post, name='post'),
    path('space', views.space, name='space'),
]
