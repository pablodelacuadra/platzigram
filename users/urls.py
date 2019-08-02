from django.urls import path
from users import views 


urlpatterns = [
    path('<str:username>/', views.UserDetailView.as_view(), name='detail'),
    path('me/profile/', views.UpdateProfileView.as_view(), name='update_profile')
]