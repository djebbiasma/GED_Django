
from django.urls import path
from . import views

urlpatterns = [
    path('login_view/', views.login_view, name='login'),
    path('logout_view/', views.logout_view, name='logout'),  
    path('register/', views.register_view, name='register'),

]