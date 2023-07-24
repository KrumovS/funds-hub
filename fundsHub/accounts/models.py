import sys

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


class Profile(models.Model):
    first_name = models.CharField(max_length=25, validators=(MinLengthValidator(2), start_with_letter,))
    last_name = models.CharField(max_length=35, validators=(MinLengthValidator(1), start_with_letter,))
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=20, validators=(MinLengthValidator(8),))
    profile_picture = models.ImageField(upload_to='assets/profile_pictures/', blank=True, null=True)
    account_level = models.ForeignKey(AccountLevel, on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name, self.last_name


