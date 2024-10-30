# Generated by Django 5.1.1 on 2024-10-29 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_account_settings_email_push_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='total_experience',
            field=models.CharField(blank=True, choices=[('Fresher', 'Fresher'), ('Below 1 year', 'Below 1 year'), ('2 years', '2 years')], max_length=150, null=True),
        ),
    ]
