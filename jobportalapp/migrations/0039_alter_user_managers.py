# Generated by Django 5.1.1 on 2024-11-05 07:01

from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0038_user'),  # Ensure the dependency is correctly referenced
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[  # If you don't need to define managers, you can leave this empty or modify it
            ],
        ),
    ]