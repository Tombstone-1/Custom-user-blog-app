from django.core.mail import send_mail
from django.conf import settings

def send_forgot_password_email(email, token):
    mail_format = f""" Hello user,
    you're receiving this email because you requested a password reset for your user account at Delicious.com with {email}. No changes have been made yet.

    if you wish to reset your password please click on the following link.
    http://127.0.0.1:8000/accounts/password_new/{token}/

    Ignore this message if you did not request the same.

    Delicious Team from django.
    """

    subject = 'Reset Password Link From Delicious.com'
    message = mail_format
    email_from = settings.EMAIL_HOST_USER
    recipient = [email]
    
    send_mail(subject, message, email_from, recipient)

    return True