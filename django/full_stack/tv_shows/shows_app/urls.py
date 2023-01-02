from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new/', views.new), 
    path('create/', views.create), # POST
    path('<int:show_id>/', views.show),
    path('<int:show_id>/edit/', views.edit),
    path('<int:show_id>/update/', views.update),# POST
    path('<int:show_id>/destroy/', views.destroy)
]
