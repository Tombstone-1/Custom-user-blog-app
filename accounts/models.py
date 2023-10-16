from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import CustomUserManager

# Customization On User Models

class CustomUser(AbstractUser):
    username = None

    gen_choice = [
        ('male', 'male'),
        ('female', 'female'),
        ('prefer not to say', 'prefer not to say'),
    ]

    # for saving and checking forgot password token when recieved in email.
    forgot_password_token = models.CharField(max_length=150, blank=True, null=True)
    
    email = models.EmailField(verbose_name='email', unique=True, blank=False, null=True)
    gender = models.CharField(verbose_name='gender', max_length=20, choices=gen_choice, blank=True, null=True)
    bio = models.CharField(verbose_name='bio', max_length=50, blank=True, null=True)
    profile_pic = models.ImageField(verbose_name='profile pic', default='profile\default_profile_pic.gif', upload_to='profile', blank=True, null=True)

    USERNAME_FIELD = 'email'  # for which you want as login credentials
    REQUIRED_FIELDS = []

    # objects is for manager for this models. you can write it here also but it good practice to seperate some stuff.
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

