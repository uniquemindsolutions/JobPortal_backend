from django.db import models
from django.contrib.auth.models import AbstractUser
from django_countries.fields import CountryField
# Create your models here.

class TotalVisitorCount(models.Model):
    visitor_count = models.IntegerField()

    def formatted_visitor_count(self):
        """Return the visitor count in a formatted string (e.g., '1.7k')."""
        if self.visitor_count >= 1000:
            return f"{self.visitor_count / 1000:.1f}k"
        return str(self.visitor_count)

class Shortlisted_Candidates(models.Model):
    shortlisted_count = models.IntegerField()

class ProfileViews(models.Model):
    profile_view = models.IntegerField()

    def formatted_profile_view(self):
        """Return the profile view count in a formatted string (e.g., '1.7k')."""
        if self.profile_view >= 1000:
            return f"{self.profile_view / 1000:.1f}k"
        return str(self.profile_view)


class Appliedjobs(models.Model):
    appliedjobs_count = models.IntegerField()

class JobView(models.Model):
    JOB_CHOICES = [
        ('mobile_web_developer', 'Mobile Web Developer'),
        ('web_developer', 'Web Developer'),
        ('python_developer', 'Python Developer'),
        ('react_developer', 'React Developer'),
    ]

    job_title = models.CharField(max_length=50, choices=JOB_CHOICES)

    def __str__(self):
        return self.get_job_title_display()
class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name
        
class Myprofile(models.Model):

    photo = models.ImageField(upload_to='Myprofile/Images',blank=True, null=True)
    employee_Name = models.CharField(max_length=80, blank=True, null=True)
    website = models.URLField()
    email = models.EmailField(max_length=254, blank=True, null=True)
    company_size = models.IntegerField()
    Founded_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=90,blank=True, null=True)
    phone_number = models.CharField(max_length=10)
    about_company = models.TextField(max_length=160,blank=True, null=True)
    address = models.TextField(max_length=180,blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    zip_code = models.IntegerField()
    map_location = models.CharField(max_length=100,blank=True, null=True)

class Submitjob(models.Model):
    Job_Category_Choices = [
        ('Ui Developer', 'Ui Developer'),
        ('React', 'React'),
        ('Angular', 'Angular')
    ]
    Job_Type_Choices = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Hourly-Contract', 'Hourly Contract'),
        ('Fixed-Price','Frice-Price')
    ]
    Salary_Choices = [
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
    ]
    # Choices for Experience
    Experience_Choices = [
        ('Expert', 'Expert'),
        ('Intermediate', 'Intermediate'),
        ('No Experience', 'No Experience')
    ]
    
    # Choices for Location (State and Capital Cities)
    Location_Choices = [
        ('Hyderabad TS', 'Hyderabad TS'),
        ('Bangalore KT ', 'Bangalore KT '),
        ('Mumbai MH','Mumbai MH'),
        ('Delhi DL','Delhi DL'),
        # Add more states and capital cities as needed
    ]

    # Choices for Industry
    Industry_Choices = [
        ('IT', 'IT'),
        ('Marketing', 'Marketing'),
        ('Software Industry', 'Software Industry'),
        ('Healthcare', 'Healthcare'),
        ('Finance', 'Finance'),
        # Add more industries as needed
    ]

    # Choices for English Fluency
    English_Fluency_Choices = [
        ('Basic', 'Basic'),
        ('Medium', 'Medium'),
        ('Excellent', 'Excellent'),
    ]

    jobtitle = models.CharField(max_length=100,blank=True, null=True)
    jobdescription = models.TextField()
    jobCategory = models.CharField(max_length=100, choices=Job_Category_Choices)
    jobtype = models.CharField(max_length=40, choices=Job_Type_Choices)
    salary = models.CharField(max_length=50, choices=Salary_Choices)
    min_salary = models.IntegerField()
    max_salary = models.IntegerField()
    skills = models.CharField(max_length=50, blank=True, null=True)
    experience = models.CharField(max_length=50, choices=Experience_Choices)
    location = models.CharField(max_length=100, choices=Location_Choices)
    Industry = models.CharField(max_length=50, choices=Industry_Choices)
    english_fluency = models.CharField(max_length=90, choices=English_Fluency_Choices)
    upload_file = models.FileField(upload_to='JobDetails/File')
    address = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
    map_location = models.CharField(max_length=100,blank=True, null=True)

class AccountSettings(models.Model):
    firstname = models.CharField(max_length=70,blank=True, null=True)
    lastname = models.CharField(max_length=70,blank=True, null=True)
    email = models.EmailField(max_length=40,blank=True, null=True)
    phone_number = models.CharField(max_length=10)

class Changepassword(models.Model):
    old_password = models.CharField(max_length=90,blank=True, null=True)
    new_password = models.CharField(max_length=90,blank=True, null=True)
    confirm_password = models.CharField(max_length=90, blank=True, null=True)
