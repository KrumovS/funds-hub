# Generated by Django 4.2.3 on 2023-08-03 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountlevel',
            name='amount',
        ),
        migrations.AddField(
            model_name='accountlevel',
            name='max_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='accountlevel',
            name='min_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accountlevel',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='accountlevel',
            name='reward',
            field=models.CharField(max_length=100),
        ),
    ]
