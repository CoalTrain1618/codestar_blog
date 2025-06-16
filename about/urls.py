from . import views
from django.urls import path


urlpatterns = [
    path('about/', views.about_detail, name='about_detail'),
]