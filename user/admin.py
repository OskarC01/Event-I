from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    create_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = [
        'email',
        'username',
        'is_staff',
        'is_superuser',
    ]
    readonly_fields = ['last_login', 'date_joined']

admin.site.register(CustomUser, CustomUserAdmin)