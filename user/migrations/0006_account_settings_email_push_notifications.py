# Generated by Django 5.1.1 on 2024-10-24 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_skills_last_used'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_settings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hide_profile_from_recruiters', models.BooleanField(default=False)),
                ('deactivate_account', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Email_Push_Notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('daily_new_jobs', models.BooleanField(default=True)),
                ('applied_jobs', models.BooleanField(default=True)),
                ('follow_up_credited', models.BooleanField(default=False)),
                ('follow_up_used', models.BooleanField(default=False)),
                ('pending_test', models.BooleanField(default=False)),
                ('promotional', models.BooleanField(default=False)),
                ('chat_notifications', models.BooleanField(default=False)),
                ('educational_notifications', models.BooleanField(default=False)),
            ],
        ),
    ]