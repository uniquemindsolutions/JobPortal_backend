# Generated by Django 5.1.1 on 2024-10-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0031_remove_myprofile_category_myprofile_functional_area_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubmitJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
