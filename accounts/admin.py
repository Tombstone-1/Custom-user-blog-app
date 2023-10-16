from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# using useradminConfig here cause will change admin panel basic fieldsets for every layout
class UserAdminConfig(UserAdmin):

    # Outer Layout of admin panel
    search_fields = ('email',)
    list_filter = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    ordering = ('-date_joined',)
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    readonly_fields = ('last_login', 'date_joined')

    # For viewing an Existing user Information.
    fieldsets = (
         # ('heading', dict{'fields' : tuple('field1','field2',)})
        ('Auth', {'fields': ('email','password')}),
        ('Personal', {'fields':('first_name', 'last_name', 'gender', 'bio', 'profile_pic')}),
        ('Status', {'fields' : ('last_login', 'date_joined')}),
        ('Permissions', {'fields' : ('is_staff', 'is_active')}),
    )
    
    # For creating newuser
    add_fieldsets = (
        (None, {
            'classes' : ('wide',),
            'fields' : ('email', 'password1', 'password2', 'first_name', 'last_name','gender', 'bio'),
        }),
    )
 
admin.site.register(CustomUser, UserAdminConfig)

# solution of using custom user and not getting hashed password.