# Generated by Django 4.2.3 on 2023-08-13 12:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_project_project_created_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='donated',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)]),
        ),
    ]