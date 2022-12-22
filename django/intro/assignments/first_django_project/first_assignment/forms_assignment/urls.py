from django.urls import path
from . import views
urlpatterns = [
    path('', views.form),
    path('save', views.save_survey),
    path('result', views.result)
]