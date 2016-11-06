from django.shortcuts import render, get_object_or_404

# Create your views here.
def profile_listen(request):
    return render(request, 'userprofile/profile-listen.html')

def profile_dibs(request):
    return render(request, 'userprofile/profile-dibs.html')

def profile_saves(request):
    return render(request, 'userprofile/profile-saves.html')

def profile_settings(request):
    return render(request, 'userprofile/profile-settings.html')

def profile_social(request):
    return render(request, 'userprofile/profile-social.html')