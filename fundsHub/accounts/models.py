import sys

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class AccountLevel(models.Model):
    name = models.CharField(max_length=30)
    min_amount = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    max_amount = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(sys.maxsize)])
    reward = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class FundsHubUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    amount_donated = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    account_level = models.ForeignKey(AccountLevel, on_delete=models.PROTECT, default=1)

    def total_donations(self):
        return self.donation_set.aggregate(total=models.Sum('amount'))['total'] or 0

    def __str__(self):
        return self.username
