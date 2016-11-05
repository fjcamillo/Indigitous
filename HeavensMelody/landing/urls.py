from django.conf.urls import url, include
from . import views

urlpatterns = [
    url('^', views.land),
    url('^signin', views.sign_in),
]