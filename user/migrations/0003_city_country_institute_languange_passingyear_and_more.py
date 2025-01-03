# Generated by Django 5.1.1 on 2024-10-24 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_userprofile_workexperience'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Languange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Languange_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='PassingYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PreferredDepartmentFunction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_departement_name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='PreferredJobTitle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferredjobtitle', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('url', models.URLField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('details_of_project', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('IT_Skills', models.CharField(max_length=120)),
                ('version', models.CharField(max_length=120)),
                ('last_used', models.DateTimeField(auto_now_add=True)),
                ('experience', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='hybrid',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='in_office',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='notice_period',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='work_from_home',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='notice_period',
            field=models.CharField(blank=True, choices=[('Immediately available', 'Immediately available'), ('15 days', '15 days'), ('30 days', '30 days'), ('45 days', '45 days'), ('2 Months', '2 Months'), ('3 Months', '3 Months')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='workexperience',
            name='workplace',
            field=models.CharField(choices=[('in_office', 'In-Office'), ('hybrid', 'Hybrid'), ('work_from_home', 'Work from Home')], default=None, max_length=150),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='current_salary',
            field=models.CharField(choices=[('INR', 'Indian Rupee (INR)'), ('USD', 'US Dollar (USD)'), ('AED', 'UAE Dirham (AED)')], max_length=50),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='current_location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_loaction', to='user.city'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='preferred_locations',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='preferred_location', to='user.city'),
        ),
        migrations.CreateModel(
            name='Language_Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proficiency', models.CharField(choices=[('Expert', 'Expert'), ('Beginner', 'Beginner'), ('Proficient', 'Proficient')], max_length=100)),
                ('languange', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.languange')),
            ],
        ),
        migrations.CreateModel(
            name='PersonDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=150, null=True)),
                ('data_of_birth', models.DateField()),
                ('category', models.CharField(choices=[('OC', 'OC'), ('General', 'General')], max_length=100)),
                ('Have_you_taken_a_career_break', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=20)),
                ('resident_status', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('work_permit_for_USA', models.CharField(choices=[('Green Card holder', 'Green Card holder')], max_length=100)),
                ('work_permit_for_other_country', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100)),
                ('i_am_specially_abled', models.BooleanField()),
                ('Nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='person_details', to='user.country')),
            ],
        ),
        migrations.CreateModel(
            name='Job_Preferences',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_type', models.CharField(blank=True, choices=[('Permanent', 'Permanent'), ('Temporary/Contract', 'Temporary/Contract'), ('Both', 'Both')], max_length=150, null=True)),
                ('employee_type', models.CharField(blank=True, choices=[('Full time', 'Full time'), ('Part time', 'Part time'), ('Both', 'Both')], max_length=150, null=True)),
                ('prefreed_workplace', models.CharField(blank=True, choices=[('In-Office', 'In-Office'), ('Hybrid', 'Hybrid'), ('Work from home', 'Work from home')], max_length=150, null=True)),
                ('what_are_you_currently_looking_for', models.CharField(blank=True, choices=[('Intership', 'Intership'), ('Job', 'Job')], max_length=150, null=True)),
                ('preferred_location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='job_preferences', to='user.city')),
                ('preferred_department_function', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.preferreddepartmentfunction')),
                ('preferred_job_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.preferredjobtitle')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='specializations', to='user.qualification')),
            ],
        ),
        migrations.CreateModel(
            name='Education_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grading_system', models.CharField(blank=True, choices=[('Scale 10 Grading System', 'Scale 10 Grading System'), ('Scale 4 Grading System', 'Scale 4 Grading System'), ('% Marks out of 100', '% Marks out of 100'), ('Course only required to pass', 'Course only required to pass')], max_length=150, null=True)),
                ('marks', models.CharField(max_length=120)),
                ('education_type', models.CharField(blank=True, choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Correspondence', 'Correspondence')], max_length=120, null=True)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.institute')),
                ('passing_year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.passingyear')),
                ('qualification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.qualification')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='states', to='user.country')),
            ],
            options={
                'unique_together': {('name', 'country')},
            },
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='user.state'),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together={('name', 'state')},
        ),
    ]
