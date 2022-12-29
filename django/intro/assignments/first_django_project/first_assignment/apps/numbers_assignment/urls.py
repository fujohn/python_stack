from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session/', views.destroy),
    path('double/', views.double),
    path('custom_add', views.add)
]