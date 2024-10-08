# Generated by Django 5.1.1 on 2024-10-07 11:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportalapp', '0016_education_ssc_submitjob_work_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='PG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pg_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ug_name', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='education',
            name='PG',
        ),
        migrations.RemoveField(
            model_name='education',
            name='UG',
        ),
        migrations.AddField(
            model_name='education',
            name='pg_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobportalapp.pg'),
        ),
        migrations.AddField(
            model_name='education',
            name='ug_course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='jobportalapp.ug'),
        ),
    ]
