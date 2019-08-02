from django.urls import path
from posts import views 


urlpatterns = [
    path(route='', view=views.PostFeedView.as_view(), name='feed'),
    path('posts/new/', views.PostCreateView.as_view(), name='create'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
]