from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import ProfileForm, SignUpForm
 
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
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    
    context = {
        'form': form
    }

    return render(request, 'users/signup.html', context)

@login_required
def update_profile_view(request):
    profile = request.user.profile
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')
    else:
        form = ProfileForm()

    context ={
        'profile': profile,
        'user': request.user,
        'form': form
    }
    return render(request, 'users/update_profile.html', context)


@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


