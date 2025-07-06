from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, SharedFile

class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('user_type',)

    # Add user_type to the fieldsets for editing users
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

    # Add user_type to add_fieldsets for creating new users
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('user_type',)}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SharedFile)
