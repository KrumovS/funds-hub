# Generated by Django 4.2.3 on 2023-08-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundshubuser',
            name='password',
            field=models.CharField(max_length=20),
        ),
    ]