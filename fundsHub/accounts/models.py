import sys

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.db import models

from fundsHub.accounts.validators import start_with_letter


class AccountLevel(models.Model):

    name = models.CharField(max_length=30)
    min_amount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    max_amount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(sys.maxsize)])
    reward = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class FundsHubUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='assets/profile_pictures/', blank=True, null=True)
    account_level = models.ForeignKey(AccountLevel, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.first_name, self.last_name


