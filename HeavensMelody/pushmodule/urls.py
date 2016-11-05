from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^published/', views.published, name='published'),
    url(r'^unfinished/', views.unfinished, name='unfinished'),
    url(r'^finished/', views.finished, name='finished'),
    url(r'^create/', views.create, name='create')

]