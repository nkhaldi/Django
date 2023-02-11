from django.urls import path

from users.views import UserRegisterView, login, profile, logout


app_name = 'users'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
