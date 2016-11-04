from django.shortcuts import render

from django.http import HttpResponse

from django.contrib.auth import authenticate, login

# Create your views here.

def index(request):
    return HttpResponse('<h1>Shaneh Leng</h1>')

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    u = authenticate(username=username, password=password)

    if u is not None:
        login(username, password)
        render(request, )