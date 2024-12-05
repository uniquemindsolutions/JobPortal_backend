from django.conf import settings
from django.db import models
from jobportalapp.models import SubmitJob, User
# Create your models here.
 
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

class PreferredDepartmentFunction(models.Model):
    preferred_departement_name = models.CharField(max_length=150)

class PreferredJobTitle(models.Model):
    preferredjobtitle = models.CharField(max_length=150)

class Years(models.Model):
    experience_level = models.CharField(max_length=50)
    def __str__(self):
        return self.experience_level
class UserProfile(models.Model):
    NOTICE_PERIOD_CHOICES = [
        ('Immediately available', 'Immediately available'),
        ('15 days', '15 days'),
        ('30 days', '30 days'),
        ('45 days', '45 days'),
        ('2 Months', '2 Months'),
        ('3 Months', '3 Months')
    ]
    Months_Choice = [
        ('1 month', '1 month'),
        ('2 months', '2 months'),
        ('3 months', '3 months'),
        ('4 months', '4 months'),
        ('5 months', '5 months'),
        ('6 months', '6 months'),
        ('7 months', '7 months'),
        ('8 months', '8 months'),
        ('9 months', '9 months'),
        ('10 months', '10 months'),
        ('11 months', '11 months'),
    ]
    profile_photo = models.ImageField(upload_to='User/Profile/images',null=True,blank=True)
    first_name = models.CharField(max_length=120)
    last_name = models.CharField(max_length=120,null=True,blank=True)
    email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=10)
    resume = models.FileField(upload_to='User/Profile/Resume',null=True,blank=True)
    industry = models.ForeignKey(PreferredDepartmentFunction,on_delete=models.SET_NULL, null=True, blank=True, related_name='industry')
    total_experience = models.ForeignKey(Years, on_delete=models.SET_NULL, null=True, blank=True, related_name='user_profiles')
    total_months = models.CharField(max_length=40,choices=Months_Choice,blank=True, null=True)
    current_location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='current_loaction')
    preferred_locations = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='preferred_location')
    notice_period = models.CharField(max_length=50, choices=NOTICE_PERIOD_CHOICES, null=True,blank=True)  # Required
    functional_area = models.ForeignKey(PreferredJobTitle,on_delete=models.SET_NULL, null=True, blank=True, related_name='functional_area')
    current_company_name = models.CharField(max_length=100,blank=True, null=True)
    
class Workexperience(models.Model):
    WORKPLACE_CHOICES = [
        ('in_office', 'In-Office'),
        ('hybrid', 'Hybrid'),
        ('work_from_home', 'Work from Home'),
        ('remote', 'Remote'),
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
    Current_Company_Choice = [
        ('Yes','Yes'),
        ('No','No')
    ]
    current_job_title = models.CharField(max_length=120)
    company_name = models.CharField(max_length=120)
    is_current_company = models.CharField(max_length=20,choices=Current_Company_Choice,null=True,blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    workplace = models.CharField(max_length=150,choices=WORKPLACE_CHOICES,null=True,blank=True)
    employment_type = models.CharField(max_length=50, choices=EMPLOYMENT_TYPE_CHOICES,blank=True,)
    currency_type = models.CharField(max_length=50,choices=Current_Salary_Choice,null=True,blank=True)
    current_salary = models.CharField(max_length=20,null=True,blank=True)
    description = models.TextField(null=True,blank=True)

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
    specialization = models.ForeignKey(Specialization, on_delete=models.CASCADE,null=True,blank=True)
    # institute = models.ForeignKey(Institute, on_delete=models.CASCADE)
    institute = models.CharField(max_length=200)
    grading_system = models.CharField(max_length=150, choices=Grading_System_Choice,null=True,blank=True)
    marks = models.CharField(max_length=120,null=True,blank=True)
    passing_year = models.DateField(null=True)  
    education_type = models.CharField(max_length=120, choices=Education_Type_Choice)

class Job_Preferences(models.Model):
    JOB_TYPE_CHOICES = [
        ('Permanent', 'Permanent'),
        ('Temporary_Contract', 'Temporary_Contract'),
        ('Both','Both')
    ]
    EMPLOYEEE_TYPE_CHOICE = [
        ('Full_time','Full_time'),
        ('Part_time','Part_time'),
        ('Both','Both')
    ]
    Preferred_Workplace_Choice = [
        ('In_Office','In_Office'),
        ('Hybrid','Hybrid'),
        ('Work_from_home','Work_from_home')
    ]
    Currently_looking_for_Choice =[
        ('Internship','Internship'),
        ('Job','Job')
    ] 
    preferred_department_function = models.ForeignKey(PreferredDepartmentFunction, on_delete=models.CASCADE)
    preferred_job_title =  models.ForeignKey(PreferredJobTitle, on_delete=models.CASCADE,null=True,blank=True)
    job_type = models.CharField(max_length=150,choices=JOB_TYPE_CHOICES, null=True,blank=True)
    employee_type = models.CharField(max_length=150,choices=EMPLOYEEE_TYPE_CHOICE, null=True,blank=True)
    prefreed_workplace = models.CharField(max_length=150,choices=Preferred_Workplace_Choice, null=True,blank=True)
    preferred_location = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True, related_name='job_preferences')
    what_are_you_currently_looking_for = models.CharField(max_length=150,choices=Currently_looking_for_Choice, null=True,blank=True)

class Skills(models.Model):
    IT_Skills  = models.CharField(max_length=120,null=True,blank=True)
    version = models.CharField(max_length=120,null=True,blank=True)
    last_used = models.DateField(null=True,blank=True)
    experience = models.IntegerField(null=True,blank=True)

class Projects(models.Model):
    title = models.CharField(max_length=120)
    url = models.URLField(null=True,blank=True)
    start_date = models.DateField(null=True,blank=True)
    end_date = models.DateField(null=True,blank=True)
    details_of_project = models.TextField(null=True,blank=True) 

class PersonDetails(models.Model):
    Gender_Choice = [
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others')
    ]
    Carrer_Break_Choice = [
        ('Yes','Yes'),
        ('No','No')
    ]
    Work_Permit_For_USA_Choice = [
        ('Green Card holder','Green Card holder'),
        ('Have L1 Visa','Have L1 Visa'),
        ('US Citizen','US Citizen'),
        ('TN Permit Holder','TN Permit Holder'),
        ('Have H1 Visa','Have H1 Visa'),
        ('I have Work Authorization','I have Work Authorization'),
        ('Authorized to work in the US','Authorized to work in the US'),
        ('No US Work authorization','No US Work authorization'),
    ]
    MARITAL_STATUS_CHOICES = [
    ('single', 'Single'),
    ('married', 'Married'),
    ('divorced', 'Divorced'),
    ('widowed', 'Widowed'),
    ('separated', 'Separated'),
    ('others', 'Others'),
    ]
    gender = models.CharField(max_length=150,choices=Gender_Choice, blank=True, null=True)
    date_of_birth = models.DateField()
    Have_you_taken_a_career_break = models.CharField(max_length=20,choices=Carrer_Break_Choice)
    resident_status = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='person_details_resident_status')
    work_permit_for_USA = models.CharField(max_length=100,choices = Work_Permit_For_USA_Choice,null=True,blank=True)
    marital_status = models.CharField(max_length=100,choices=MARITAL_STATUS_CHOICES,null=True,blank=True)
    work_permit_for_other_country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='person_details_country')
    Nationality = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True, blank=True, related_name='person_details')
    i_am_specially_abled = models.BooleanField()

class Language(models.Model):
    language_name = models.CharField(max_length=200)

class Language_Page(models.Model):
    Proficiency_Choice = [
        ('Expert', 'Expert'),
        ('Beginner', 'Beginner'),
        ('Proficient', 'Proficient')
    ]
    LanguageSkillChoice = [
        ('Read', 'Read'),
        ('Write', 'Write'),
        ('Speak', 'Speak'),
    ]
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    proficiency = models.CharField(max_length=100, choices=Proficiency_Choice, null=True, blank=True)
    languageskill = models.CharField(max_length=100, choices=LanguageSkillChoice, null=True, blank=True)


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

class SavedJobs(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applied_jobs")
    job_id = models.ForeignKey(SubmitJob, on_delete=models.CASCADE, related_name="applications")
    
    class Meta:
        unique_together = ('user_id', 'job_id')  # Use the exact field names

    def __str__(self):
        return f"User {self.user_id} saved Job {self.job_id}"