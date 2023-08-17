# Generated by Django 4.2.3 on 2023-08-18 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_fundshubuser_user_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountlevel',
            name='max_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='accountlevel',
            name='min_amount',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fundshubuser',
            name='account_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.accountlevel'),
        ),
        migrations.AlterField(
            model_name='fundshubuser',
            name='amount_donated',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='fundshubuser',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to='profile_pictures/'),
        ),
    ]
