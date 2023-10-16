from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout as auth_logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserSignupForm
from .models import CustomUser as custom_user
from .helpers import send_forgot_password_email
import uuid

# Create your views here.

############################## AUTHENTICATE #########################
# django login, logout and login, logout method name can't be same. change either one of them.

@login_required(login_url="/")
def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
        messages.success(request, "Sign out successfully")
        return redirect("/")
    else:
        return redirect("/")

def login(request):
    if request.user.is_authenticated:
        messages.info(request, f"you are already logged in as {request.user.email}. ")
        return redirect("/")
    
    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        if not email or not password:
            messages.warning(request, "Both Email and Password are required ")
            return redirect("accounts/login")
        else:
            user = authenticate(email = email, password = password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"you are logged in as {email}.")
            return redirect("/")
        else:
            messages.error(request, "login failed. Incorrect Email or Password")
            return redirect("/accounts/login")
        
    return render(request, 'accounts/login.html')

def signup(request):
    form = CustomUserSignupForm()

    if request.method == 'POST':
        form = CustomUserSignupForm(request.POST)
        email = request.POST.get('email').lower()
        
        try:
            user = custom_user.objects.get(email = email)
            messages.warning(request, "email already exists")
        except custom_user.DoesNotExist:
            if form.is_valid():
                user = form.save(commit=False)
                user.email = user.email.lower()
                user.save()
                messages.success(request, "User signup successfully")
                return redirect("/accounts/login")
            else:
                messages.warning(request, "signup Unsuccessful")

    context = {'signup_form':form}
    return render(request, 'accounts/signup.html', context)

def reset_passwordlink(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        user_email = custom_user.objects.filter(email = email).first()

        if user_email is not None:
            # generating unique id for user identification.
            token = str(uuid.uuid4())

            # Saving token for later matching.
            user_obj = custom_user.objects.get(email = user_email)
            user_obj.forgot_password_token = token
            user_obj.save()
            try:
                send_forgot_password_email(user_email, token)
            except Exception as e:
                print(e)
            messages.success(request, f"reset email has been sent to {user_email}")
            return redirect("/accounts/password_reset")
        else:
            messages.error(request,'please enter correct email to get a reset link')
            return redirect("/accounts/password_reset")
        
    return render(request, 'accounts/password_reset.html')

def reset_newpassword(request, token):

    user_obj = custom_user.objects.filter(forgot_password_token = token).first()
    context = {'user_id' : user_obj.id}
    
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        new_password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')

        if new_password == confirm_password:
            if user_id is not None:
                user_obj = custom_user.objects.get(id = user_id)
                user_obj.set_password(new_password)
                user_obj.save()
                messages.success(request, "password reset successfully.")
                return redirect(f'/accounts/login')
            else:
                messages.error(request, "User ID not found")
                return redirect(f'/accounts/password_new/{token}')
        else:
            messages.error(request, "both password should be same")
            return redirect(f'/accounts/password_new/{token}')

    return render(request, 'accounts/password_new.html', context)