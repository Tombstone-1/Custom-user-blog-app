from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create_post/', views.create_post, name='create_post'),
    path('update_post/<pk>', views.update_post, name='update_post'),
    path('delete_post/<pk>', views.delete_post, name='delete_post'),
]