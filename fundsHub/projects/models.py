import sys

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Project(models.Model):
    name = models.CharField(max_length=200)
    short_description = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='assets/projects_pictures/')
    funding_goal = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.0)])
    long_description = models.TextField()
    project_end_date = models.DateField()

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"


class ProjectCompleteness(models.Model):
    min_percentage = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    max_percentage = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(sys.maxsize)])
    description = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Project Completeness"
