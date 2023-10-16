from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('password_reset/', views.reset_passwordlink, name='password_reset'),
    path('password_new/<token>/', views.reset_newpassword, name='password_new')
]