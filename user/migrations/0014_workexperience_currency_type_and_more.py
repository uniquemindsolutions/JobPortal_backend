# Generated by Django 5.1.1 on 2024-11-13 07:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_rename_data_of_birth_persondetails_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='currency_type',
            field=models.CharField(blank=True, choices=[('INR', 'Indian Rupee (INR)'), ('USD', 'US Dollar (USD)'), ('AED', 'UAE Dirham (AED)')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='education_details',
            name='education_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Correspondence', 'Correspondence')], default=None, max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education_details',
            name='institute',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='education_details',
            name='marks',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='education_details',
            name='specialization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.specialization'),
        ),
        migrations.AlterField(
            model_name='job_preferences',
            name='employee_type',
            field=models.CharField(blank=True, choices=[('Full_time', 'Full_time'), ('Part_time', 'Part_time'), ('Both', 'Both')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='job_preferences',
            name='job_type',
            field=models.CharField(blank=True, choices=[('Permanent', 'Permanent'), ('Temporary_Contract', 'Temporary_Contract'), ('Both', 'Both')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='job_preferences',
            name='preferred_job_title',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='user.preferredjobtitle'),
        ),
        migrations.AlterField(
            model_name='job_preferences',
            name='prefreed_workplace',
            field=models.CharField(blank=True, choices=[('In_Office', 'In_Office'), ('Hybrid', 'Hybrid'), ('Work_from_home', 'Work_from_home')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='job_preferences',
            name='what_are_you_currently_looking_for',
            field=models.CharField(blank=True, choices=[('Internship', 'Internship'), ('Job', 'Job')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='language_page',
            name='proficiency',
            field=models.CharField(blank=True, choices=[('Expert', 'Expert'), ('Beginner', 'Beginner'), ('Proficient', 'Proficient')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='persondetails',
            name='marital_status',
            field=models.CharField(blank=True, choices=[('single', 'Single'), ('married', 'Married'), ('divorced', 'Divorced'), ('widowed', 'Widowed'), ('separated', 'Separated'), ('other', 'Other')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='persondetails',
            name='work_permit_for_USA',
            field=models.CharField(blank=True, choices=[('Green Card holder', 'Green Card holder'), ('Have L1 Visa', 'Have L1 Visa'), ('US Citizen', 'US Citizen'), ('TN Permit Holder', 'TN Permit Holder'), ('Have H1 Visa', 'Have H1 Visa'), ('I have Work Authorization', 'I have Work Authorization'), ('Authorized to work in the US', 'Authorized to work in the US'), ('No US Work authorization', 'No US Work authorization')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='details_of_project',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='projects',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='IT_Skills',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='experience',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='last_used',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='skills',
            name='version',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='User/Profile/images'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to='User/Profile/Resume'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='current_salary',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='is_current_company',
            field=models.BooleanField(blank=True, default='True', null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='workplace',
            field=models.CharField(blank=True, choices=[('in_office', 'In-Office'), ('hybrid', 'Hybrid'), ('work_from_home', 'Work from Home')], max_length=150, null=True),
        ),
    ]