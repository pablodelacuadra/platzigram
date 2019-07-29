from django.shortcuts import render, redirect
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Profile
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            context = {
                'error': 'Invalid username and password'
            }
            return render(request, 'users/login.html', context)
    return render(request, 'users/login.html')


def signup_view(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        password_conf = request.POST.get('password_conf', None)
        first_name = request.POST.get('first_name', None)
        last_name = request.POST.get('last_name', None)
        email = request.POST.get('email', None)

        if password != password_conf:
            context['error'] = 'Password confirmation does not match'

        try:
            user = User.objects.create_user(username=username, password=password)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            Profile.objects.create(user=user)
            return redirect('login')
        except IntegrityError:
            context['error'] = 'Username is already in use'

    return render(request, 'users/signup.html', context)


def update_profile_view(request):
    return render(request, 'users/update_profile.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


