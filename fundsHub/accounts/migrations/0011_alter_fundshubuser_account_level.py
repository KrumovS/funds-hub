# Generated by Django 4.2.3 on 2023-08-18 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_alter_accountlevel_max_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fundshubuser',
            name='account_level',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='accounts.accountlevel'),
        ),
    ]