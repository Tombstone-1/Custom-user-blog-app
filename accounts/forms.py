from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

# create your forms here.
# for User registration Only.

class CustomUserSignupForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", "password1", "password2")
