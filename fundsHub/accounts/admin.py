from django.contrib import admin

from fundsHub.accounts.models import AccountLevel, Profile


class AccountLevelAdmin(admin.ModelAdmin):
    list_display = ("name", "min_amount", "max_amount", "reward")


class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "account_level")


admin.site.register(AccountLevel, AccountLevelAdmin)
admin.site.register(Profile, ProfileAdmin)
