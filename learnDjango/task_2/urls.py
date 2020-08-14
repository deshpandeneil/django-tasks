# Created by Neil

from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='sign-up'),
    path('user-home', views.userHome, name='user-home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('search', views.search, name='search'),
]
