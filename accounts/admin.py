from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import Account


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login',
                    'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ('groups', 'user_permissions',)
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)
