from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView


from .models import Post
from .forms import PostForm

# Create your views here.


class PostFeedView(LoginRequiredMixin, ListView):
    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 20
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    template_name = 'posts/detail.html'
    slug_field = 'pk'
    slug_url_kwarg = 'pk'
    queryset = Post.objects.all()
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context 

