from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    # path('camera/', views.process_image, name='process_image'),
]