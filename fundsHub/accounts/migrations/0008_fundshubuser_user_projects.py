# Generated by Django 4.2.3 on 2023-08-13 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_userprojects_userproject'),
        ('accounts', '0007_alter_fundshubuser_profile_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='fundshubuser',
            name='user_projects',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='projects.userproject'),
        ),
    ]
