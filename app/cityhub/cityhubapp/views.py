from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *

# Create your views here.

@login_required
def home(request):
    context = {
        'posts_list': Post.objects.all().order_by("-created_at"),
        'user_recommendations': CustomUser.objects.filter(is_staff=False).exclude(id=request.user.id)
    }
    return render(request, "home.html", context)

@login_required
def create_event(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        loggedInUser = CustomUser.objects.get(id=request.user.id)
        print('Creating event', title, text, loggedInUser.username)
        Post.objects.create(type='event', title=title, text=text, published_by=loggedInUser)
        return JsonResponse({'status': 'Success', 'message': 'Data saved successfully'})
    else:
        return JsonResponse({'status': 'Error', 'message': 'Invalid request'}, status=400)
    
@login_required
def create_complaint(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        loggedInUser = CustomUser.objects.get(id=request.user.id)
        print('Creating event', title, text, loggedInUser.username)
        Post.objects.create(type='complaint', title=title, text=text, published_by=loggedInUser)
        return JsonResponse({'status': 'Success', 'message': 'Data saved successfully'})
    else:
        return JsonResponse({'status': 'Error', 'message': 'Invalid request'}, status=400)

@login_required
def profile(request):
    context = {
        'user_posts': Post.objects.filter(published_by=request.user.id)
    }
    return render(request, "profile.html", context)

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')
