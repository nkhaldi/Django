from django.urls import path

from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('point1/', views.point1, name='point-1'),
    path('point2/', views.point2, name='point-2'),
]
