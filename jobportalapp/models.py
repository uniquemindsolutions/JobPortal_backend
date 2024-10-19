from django.db import models
from django.contrib.auth.models import AbstractUser

# Model to track total visitor counts
class TotalVisitorCount(models.Model):
    visitor_count = models.IntegerField()

    def formatted_visitor_count(self):
        """Return the visitor count in a formatted string (e.g., '1.7k')."""
        if self.visitor_count >= 1000:
            return f"{self.visitor_count / 1000:.1f}k"
        return str(self.visitor_count)

# Model to track shortlisted candidates
class Shortlisted_Candidates(models.Model):
    shortlisted_count = models.IntegerField()

# Model to track profile views
class ProfileViews(models.Model):
    profile_view = models.IntegerField()

    def formatted_profile_view(self):
        """Return the profile view count in a formatted string (e.g., '1.7k')."""
        if self.profile_view >= 1000:
            return f"{self.profile_view / 1000:.1f}k"
        return str(self.profile_view)

# Model to track applied jobs
class AppliedJobs(models.Model):
    appliedjobs_count = models.IntegerField()

# Model to store job views
class JobView(models.Model):
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return self.job_title

# Model for country
# Model for country
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


# Profile model with foreign keys to Country, State, and City
class MyProfile(models.Model):
    photo = models.ImageField(upload_to='MyProfile/Images', blank=True, null=True)
    employee_name = models.CharField(max_length=80)
    website = models.URLField()
    email = models.EmailField(max_length=254)
    company_size = models.IntegerField()
    founded_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=90)
    phone_number = models.CharField(max_length=10)
    about_company = models.TextField(max_length=160)
    address = models.TextField(max_length=180)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='my_profiles')
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True, blank=True, related_name='my_profiles')
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='my_profiles')
    zip_code = models.IntegerField()
    map_location = models.CharField(max_length=100, blank=True, null=True)

# Job category model
class JobCategory(models.Model):
    job_category = models.CharField(max_length=150)

    def __str__(self):
        return self.job_category

# Industry model
class Industry(models.Model):
    industry = models.CharField(max_length=100)

    def __str__(self):
        return self.industry

class Intermediate(models.Model):
    inter = models.CharField(max_length=120, blank=True, null=True)

class UG(models.Model):
    ug_name = models.CharField(max_length=150, blank=True, null=True)

class PG(models.Model):
    pg_name = models.CharField(max_length=150, blank=True, null=True)

# Submit job model with all the necessary details
class SubmitJob(models.Model):
    JOB_TYPE_CHOICES = [
        ('Full Time', 'Full Time'),
        ('Part Time', 'Part Time'),
        ('Hourly-Contract', 'Hourly Contract'),
        ('Fixed-Price', 'Fixed-Price')
    ]
    SALARY_CHOICES = [
        ('Monthly', 'Monthly'),
        ('Weekly', 'Weekly'),
    ]
    EXPERIENCE_CHOICES = [
        ('Expert', 'Expert'),
        ('Intermediate', 'Intermediate'),
        ('No Experience', 'No Experience')
    ]
    ENGLISH_FLUENCY_CHOICES = [
        ('Basic', 'Basic'),
        ('Medium', 'Medium'),
        ('Excellent', 'Excellent'),
    ]
    WORK_MODE_CHOICES = [
        ('Work from office', 'Work from office'),
        ('Work from Home','Work from Home'),
        ('Remote', 'Remote'),
        ('Hybrid', 'Hybrid')
    ]
    SCHOOLING_CHOICE = [
        ('SSC','SSC')
    ]
    job_title = models.CharField(max_length=100)  # Required
    number_of_positions = models.IntegerField(default=0)
    job_description = models.TextField()  # Required
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)
    job_category = models.ForeignKey(JobCategory, on_delete=models.CASCADE)
    job_type = models.CharField(max_length=40, choices=JOB_TYPE_CHOICES)  
    salary_type = models.CharField(max_length=50, choices=SALARY_CHOICES)  
    min_salary = models.IntegerField(blank=True, null=True)  # Optional
    max_salary = models.IntegerField(blank=True, null=True)  # Optional
    skills = models.CharField(max_length=50, blank=True, null=True)  # Required
    experience = models.CharField(max_length=50, choices=EXPERIENCE_CHOICES, blank=True, null=True)  # Required
    city_location = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True, related_name='job_location_set')  # Required
    english_fluency = models.CharField(max_length=90, choices=ENGLISH_FLUENCY_CHOICES,null=True, blank=True)  # Optional
    # upload_file = models.FileField(upload_to='JobDetails/File', blank=True, null=True)  # Optional
    about_company = models.TextField(blank=True, null=True)
    work_mode =  models.CharField(max_length=50,choices=WORK_MODE_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
    address = models.TextField()  # Required
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True)  # Required
    state = models.ForeignKey('State', on_delete=models.SET_NULL, null=True, blank=True)  # Required
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True, related_name='job_city_set')  # Required
    ssc = models.CharField(max_length=50, choices=SCHOOLING_CHOICE, blank=True, null=True)
    intermediate = models.ForeignKey(Intermediate, on_delete=models.SET_NULL, null=True, blank=True)
    ug_course = models.ForeignKey(UG, on_delete=models.SET_NULL, null=True, blank=True)
    pg_course = models.ForeignKey(PG, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.IntegerField(default=0)

    def formatted_created_date(self):
        return self.created_date.strftime('%d-%m-%Y') 
    
    def __str__(self):
        return self.job_title

# Account settings model for user profile
class AccountSettings(models.Model):
    firstname = models.CharField(max_length=70)
    lastname = models.CharField(max_length=70)
    email = models.EmailField(max_length=40)
    phone_number = models.CharField(max_length=10)

class ChangePassword(models.Model):
    old_password = models.CharField(max_length=90)
    new_password = models.CharField(max_length=90)
    confirm_password = models.CharField(max_length=90)    

class ProfilePhoto(models.Model):
    profile_photo = models.ImageField(upload_to='profile_photos/')