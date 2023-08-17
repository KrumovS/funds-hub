from django.contrib.auth.models import AbstractUser
from django.db import models


class AccountLevel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    min_amount = models.PositiveIntegerField()
    max_amount = models.PositiveIntegerField(null=True, blank=True)
    reward = models.CharField(max_length=150)

    class Meta:
        ordering = ['min_amount']

    def __str__(self):
        return self.name


class FundsHubUser(AbstractUser):
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)
    amount_donated = models.PositiveIntegerField(default=0)

    @property
    def account_level(self):
        level = AccountLevel.objects.filter(
            min_amount__lte=self.amount_donated,
            max_amount__gt=self.amount_donated
        ).first()

        if not level and self.amount_donated:
            level = AccountLevel.objects.filter(
                min_amount__lte=self.amount_donated,
                max_amount__isnull=True
            ).first()

        return level


    @property
    def total_donations(self):
        return self.donation_set.aggregate(total=models.Sum('amount'))['total'] or 0

    def __str__(self):
        return self.username
