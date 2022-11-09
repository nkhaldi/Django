from django.urls import path
from . import views


urlpatterns = [
    path('', views.profiles, name="profiles"),
    path('login/', views.loginUser, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.userAccount, name="account"),
    path('register/', views.registerUser, name="register"),
    path('edit-account/', views.editAccount, name="edit-account"),
    path('create-skill/', views.createSkill, name="create-skill"),
    path('skill/<slug:skill_slug>', views.profiles_by_skill, name="skill"),
    path('profile/<str:username>/', views.userProfile, name="user-profile"),
    path('update-skill/<slug:skill_slug>/', views.updateSkill, name="update-skill"),
    path('delete-skill/<slug:skill_slug>/', views.deleteSkill, name="delete-skill"),
]
