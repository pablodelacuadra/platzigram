from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm

# Create your views here.


@login_required
def list_posts(request):
    posts = Post.objects.all().order_by('-created')
    
    context = {
        'posts': posts
    }
    
    return render(request, 'posts/feed.html', context)

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = PostForm()
    
    context = {
        'form': form,
        'user': request.user,
        'profile': request.user.profile
    }

    return render(request, 'posts/new.html', context)

