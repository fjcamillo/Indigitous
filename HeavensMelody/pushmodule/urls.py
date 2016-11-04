from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.index),
    url(r'^published/', views.published),
    url(r'^unfinished/', views.unfinished),
    url(r'^finished/', views.finished),
    url(r'^create/', views.create)
]