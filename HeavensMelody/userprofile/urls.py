from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.profile_listen),
    url(r'^dibs/', views.profile_dibs),
    url(r'^saves/', views.profile_saves),
    url(r'^settings/', views.profile_settings),
    url(r'^social/', views.profile_social),
]