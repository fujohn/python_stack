from django.urls import path
from . import views
urlpatterns = [
    path('register/', views.process),
    path('login/', views.login),
    path('users/new/', views.process),
    path('users/', views.show),
    path('', views.reroute)
]