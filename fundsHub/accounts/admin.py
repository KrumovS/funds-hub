from django.contrib import admin

from fundsHub.accounts.models import AccountLevel, FundsHubUser


class AccountLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "min_amount", "max_amount", "reward")


class FundsHubUserAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "account_level")


admin.site.register(AccountLevel, AccountLevelAdmin)
admin.site.register(FundsHubUser, FundsHubUserAdmin)
