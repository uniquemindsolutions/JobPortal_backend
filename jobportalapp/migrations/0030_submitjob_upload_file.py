# Generated by Django 5.1.1 on 2024-10-24 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0029_alter_submitjob_industry_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='submitjob',
            name='upload_file',
            field=models.FileField(blank=True, null=True, upload_to='JobDetails/File'),
        ),
    ]
