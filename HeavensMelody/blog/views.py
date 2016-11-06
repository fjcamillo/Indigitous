from django.shortcuts import render, get_object_or_404

# Create your views here.

def blog(request):

    return render(request, 'blog/blog.html')
