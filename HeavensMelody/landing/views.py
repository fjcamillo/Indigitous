from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse('<h1>ROMMEL REYES</h1>')

def land(request):
    if request.method == "POST":
        return render(request, 'landing/registration.html')
    return render(request, 'landing/index.html')

def registerme(request):

    return render(request, 'landing/registration.html')
