from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Frank Anthony</h1>')

def published(request):
    pass
    # return render(request, '')

def unfinished(request):
    pass
    # return render(request, '')

def finished(request):
    pass
    # return render(request, '')

def create(request):
    pass
    # return render(request, '')

