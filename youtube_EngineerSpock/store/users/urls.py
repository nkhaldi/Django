from django.contrib.auth.decorators import login_required
from django.urls import path

from users.views import login, UserRegisterView, UserPrifileView, logout


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', login_required(UserPrifileView.as_view()), name='profile'),
    path('logout/', logout, name='logout'),
]
