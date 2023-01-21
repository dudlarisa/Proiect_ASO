from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('login_user', views.login_user, name='login'),
    path('', views.home, name='home'),

    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

