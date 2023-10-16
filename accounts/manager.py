# use this base_user and not models import BaseUserManager
# using = self._db means use default database from settings.py and if any other database with "new_users" db name then using="new_users"

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _

# Custom User model Manager Written here.

class CustomUserManager(BaseUserManager):
    # this will make sure django use custom model in migrations
    use_in_migrations = True
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User Must have an Email address.")
        
        # normalize means removing case-sensitivity by putting every letter in lowercase.
        user = self.model(
            email = self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db) 
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_("Superuser must have is_staff = True"))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_("superuser must have is_superuser = True"))

        return self.create_user(email, password, **extra_fields)
    
