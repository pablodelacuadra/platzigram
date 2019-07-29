from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Utilities
from datetime import datetime
# Create your views here.

posts = [
    {
        'title': 'Mont Blac',
        'user': {
            'name': 'Yesica Cortes',
            'picture': 'https://picsum.photos/60/60/?image=1027/'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/300/?image=1036/',
    },
    {
        'title': 'Via Lactea',
        'user': {
            'name': 'C. Vander',
            'picture': 'https://picsum.photos/60/60/?image=1005/'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=903/',
    },
    {
        'title': 'Nuevo Auditorio',
        'user': {
            'name': 'Thespianartist',
            'picture': 'https://picsum.photos/60/60/?image=883/'
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'photo': 'https://picsum.photos/200/200/?image=1076/',
    },
]


@login_required
def list_posts(request):
    context = {
        'posts': posts
    }
    return render(request, 'posts/feed.html', context)
