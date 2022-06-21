from django.urls import path
from . import views

urlpatterns = [
    path('uploadUrl', views.uploadUrl, name='uploadUrl'),
    path('uploadImage', views.uploadImage, name='uploadImage'),
]