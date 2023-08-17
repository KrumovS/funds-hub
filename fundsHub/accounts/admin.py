from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from fundsHub.accounts.models import AccountLevel, FundsHubUser


class AccountLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "min_amount", "max_amount", "reward")


class FundsHubUserAdmin(UserAdmin):
    list_display = ("username", "email")
    filter_horizontal = ('groups', 'user_permissions',)

    def get_readonly_fields(self, request, obj=None):
        readonly_fields = super(FundsHubUserAdmin, self).get_readonly_fields(request, obj)
        if not request.user.is_superuser:
            return readonly_fields + ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        return readonly_fields


admin.site.register(AccountLevel, AccountLevelAdmin)
admin.site.register(FundsHubUser, FundsHubUserAdmin)
