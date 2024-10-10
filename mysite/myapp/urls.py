from django.contrib import admin
from django.urls import path,include
from . import views
from  django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.index ,name='index'),
    path('login/',LoginView.as_view(template_name='myapp/login.html'),name='login'),
    path('logout/',LogoutView.as_view(template_name='myapp/logut.html'),name='logout'),
    path('<slug:slug>/',views.chatroom,name='chatroom'),
]


