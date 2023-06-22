from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import UserChangeForm, UserCreationFrom
from .models import User 


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationFrom
    
    list_display = ('full_name', 'email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    
    fieldsets = (
        (None, {'fields': ('full_name', 'email', 'phone_number', 'password')}),
        ('permissions', {'fields': ('is_admin', 'is_active', 'last_login')})
    )
    
    add_fieldsets = (
        (None, {'fields': ('full_name', 'email', 'phone_number', 'password1', 'password2')}),
    )
    
    search_fields = ('full_name', 'email')
    ordering = ('full_name',)
    filter_horizontal = ()
    
    
admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
