# Generated by Django 4.2.3 on 2023-08-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_project_project_created_on'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]