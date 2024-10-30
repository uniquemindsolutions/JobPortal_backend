from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='user')

    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    
class Appliedjobs(models.Model):
    applied_count = models.IntegerField()

class Jobalerts(models.Model):
    jobalert_count = models.IntegerField()

class Message(models.Model):
    message_count = models.IntegerField()

class Shortlist(models.Model):
    shortlist_count = models.IntegerField()

class UserChangePassword(models.Model):
    old_password = models.CharField(max_length=90)
    new_password = models.CharField(max_length=90)
    confirm_password = models.CharField(max_length=90)  

class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensure country name is unique

    def __str__(self):
        return self.name


# Model for state, linked to a country
class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    class Meta:
        unique_together = ('name', 'country')  # Ensure state is unique per country

    def __str__(self):
        return self.name


# Model for city, linked to a state
class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    class Meta:
        unique_together = ('name', 'state')  # Ensure city is unique per state

    def __str__(self):
        return self.name
    
class UserProfile(models.Model):
    NOTICE_PERIOD_CHOICES = [
        ('Immediately available', 'Immediately available'),
        ('15 days', '15 days'),
        ('30 days', '30 days'),
        ('45 days', '45 days'),
        ('2 Months', '2 Months'),
        ('3 Months', '3 Months')
    ]
    Experience_Choice = [
        ('Fresher', 'Fresher'),	
        ('Below 1 year', 'Below 1 year'),
        ('2 years', '2 years'),
    ]
    profile_photo = models.ImageField(upload_to='User/Profile/images')
    first_name = models.CharField(max_length=120, blank=True,null=True)
    last_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=10)
    resume = models.FileField(upload_to='User/Profile/Resume')
    total_experience = models.CharField(max_length=150, choices=Experience_Choice, blank=True, null=True)  # Required
    current_location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='current_loaction')
    preferred_locations = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='preferred_location')
    notice_period = models.CharField(max_length=50, choices=NOTICE_PERIOD_CHOICES, blank=True, null=True)  # Required

class Workexperience(models.Model):
    WORKPLACE_CHOICES = [
        ('in_office', 'In-Office'),
        ('hybrid', 'Hybrid'),
        ('work_from_home', 'Work from Home'),
    ]
    EMPLOYMENT_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Internship', 'Internship'),
        ('Freelance', 'Freelance'),
    ]
    Current_Salary_Choice = [
    ('INR', 'Indian Rupee (INR)'),
    ('USD', 'US Dollar (USD)'),
    ('AED', 'UAE Dirham (AED)'),
    ]
    current_job_title = models.CharField(max_length=120)
    company_name = models.CharField(max_length=120)
    is_current_company = models.BooleanField(default='True')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    workplace = models.CharField(max_length=150,choices=WORKPLACE_CHOICES)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES, blank=True, null=True)
    current_salary = models.CharField(max_length=50,choices=Current_Salary_Choice)
    description = models.TextField()

class Qualification(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Specialization(models.Model):
    qualification = models.ForeignKey(Qualification, related_name='specializations', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.qualification.name})"

class Institute(models.Model):
    institute_name = models.CharField(max_length=120)

    def __str__(self):
        return self.institute_name
    
class Education_Details(models.Model):
    Grading_System_Choice = [
        ('Scale 10 Grading System', 'Scale 10 Grading System'),
        ('Scale 4 Grading System', 'Scale 4 Grading System'),
        ('% Marks out of 100', '% Marks out of 100'),
        ('Course only required to pass', 'Course only required to pass')
    ] 
    Education_Type_Choice = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Correspondence', 'Correspondence')
    ]
    
    qualification = models.ForeignKey(Qualification, on_delete=models.CASCADE)
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE)
    institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    grading_system = models.CharField(max_length=150, choices=Grading_System_Choice, blank=True, null=True)
    marks = models.CharField(max_length=120)
    passing_year = models.BigIntegerField(null=True)  # Existing field
    passing_year_temp = models.DateTimeField(null=True)  # New temporary field
    education_type = models.CharField(max_length=120, choices=Education_Type_Choice, blank=True, null=True)


class PreferredDepartmentFunction(models.Model):
    preferred_departement_name = models.CharField(max_length=150)

class PreferredJobTitle(models.Model):
    preferredjobtitle = models.CharField(max_length=150)

class Job_Preferences(models.Model):
    JOB_TYPE_CHOICES = [
        ('Permanent', 'Permanent'),
        ('Temporary/Contract', 'Temporary/Contract'),
        ('Both','Both')
    ]
    EMPLOYEEE_TYPE_CHOICE = [
        ('Full time','Full time'),
        ('Part time','Part time'),
        ('Both','Both')
    ]
    Preferred_Workplace_Choice = [
        ('In-Office','In-Office'),
        ('Hybrid','Hybrid'),
        ('Work from home','Work from home')
    ]
    Currently_looking_for_Choice =[
        ('Intership','Intership'),
        ('Job','Job')
    ] 
    preferred_department_function = models.ForeignKey(PreferredDepartmentFunction, on_delete=models.CASCADE)
    preferred_job_title =  models.ForeignKey(PreferredJobTitle, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=150,choices=JOB_TYPE_CHOICES, blank=True, null=True)
    employee_type = models.CharField(max_length=150,choices=EMPLOYEEE_TYPE_CHOICE, blank=True, null=True)
    prefreed_workplace = models.CharField(max_length=150,choices=Preferred_Workplace_Choice, blank=True, null=True)
    preferred_location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='job_preferences')
    what_are_you_currently_looking_for = models.CharField(max_length=150,choices=Currently_looking_for_Choice, blank=True, null=True)

class Skills(models.Model):
    IT_Skills  = models.CharField(max_length=120)
    version = models.CharField(max_length=120)
    last_used = models.DateTimeField()
    experience = models.IntegerField()

class Projects(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    details_of_project = models.TextField() 

class PersonDetails(models.Model):
    Gender_Choice = [
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    ]
    Category_Choice = [
        ('OC','OC'),
        ('General','General'),
    ]
    Carrer_Break_Choice = [
        ('Yes','Yes'),
        ('No','No')
    ]
    Resident_Status_Choice = [
        ('Yes','Yes'),
        ('No','No'),
    ]
    Work_Permit_For_USA_Choice = [
        ('Green Card holder','Green Card holder'),
    ]
    Work_Permit_For_Other_Country_Choice=[
        ('Yes','Yes'),
        ('No','No'),
    ]
    gender = models.CharField(max_length=150,choices=Gender_Choice, blank=True, null=True)
    data_of_birth = models.DateField()
    category = models.CharField(max_length=100,choices=Category_Choice)
    Have_you_taken_a_career_break = models.CharField(max_length=20,choices=Carrer_Break_Choice)
    resident_status = models.CharField(max_length=100,choices=Resident_Status_Choice)
    work_permit_for_USA = models.CharField(max_length=100,choices = Work_Permit_For_USA_Choice)
    work_permit_for_other_country = models.CharField(max_length=100,choices=Work_Permit_For_Other_Country_Choice)
    Nationality = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='person_details')
    i_am_specially_abled = models.BooleanField()

class Languange(models.Model):
    Languange_name = models.CharField(max_length=200)

class Language_Page(models.Model):
    Proficiency_Choice = [
        ('Expert','Expert'),
        ('Beginner','Beginner'),
        ('Proficient','Proficient')
    ]
    languange =models.ForeignKey(Languange, on_delete=models.SET_NULL,null=True, blank=True)
    proficiency = models.CharField(max_length=100,choices = Proficiency_Choice)


class Email_Push_Notifications(models.Model): 
    daily_new_jobs = models.BooleanField(default=True)
    applied_jobs = models.BooleanField(default=True)
    follow_up_credited = models.BooleanField(default=False)
    follow_up_used = models.BooleanField(default=False)
    pending_test = models.BooleanField(default=False)
    promotional = models.BooleanField(default=False)
    chat_notifications = models.BooleanField(default=False)
    educational_notifications = models.BooleanField(default=False)

class Account_settings(models.Model):
    hide_profile_from_recruiters = models.BooleanField(default=False)
    deactivate_account = models.BooleanField(default=False)


