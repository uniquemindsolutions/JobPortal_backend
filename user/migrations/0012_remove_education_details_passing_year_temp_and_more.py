# Generated by Django 5.1.1 on 2024-11-07 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_persondetails_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='education_details',
            name='passing_year_temp',
        ),
        migrations.AddField(
            model_name='persondetails',
            name='marital_status',
            field=models.CharField(choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('other', 'Other')], default=None, max_length=100),
            preserve_default=False,
        ),
    ]
