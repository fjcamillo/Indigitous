from django.shortcuts import render, get_object_or_404
from .models import create
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('<h1>Frank Anthony</h1>')

def published(request):
    context_index = {

    }
    return render(request, '', context_index)

def unfinished(request):
    context_index = {

    }
    return render(request, '', context_index)

def finished(request):
    context_index = {

    }
    return render(request, '', context_index)

def create(request):
    context_index = {

    }
    return render(request, 'pushmodule/push-create.html', context_index)

