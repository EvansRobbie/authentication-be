from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserAccount

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        # ... your fieldsets ...
    )
    add_fieldsets = (
        # ... your add_fieldsets ...
    )

    list_display = ('email', 'name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff')

    search_fields = ('email', 'name')
    ordering = ('email',)

admin.site.register(UserAccount, UserAdmin)