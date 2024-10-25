from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
# Register your models here.
class CustomUserAdmin(UserAdmin):
    model = CustomUser
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Appliedjobs)
admin.site.register(Jobalerts)
admin.site.register(Message)
admin.site.register(Shortlist)
admin.site.register(UserChangePassword)
admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)
admin.site.register(UserProfile)
admin.site.register(Workexperience)
admin.site.register(Qualification)
admin.site.register(Specialization)
admin.site.register(Institute)
admin.site.register(Education_Details)
admin.site.register(PreferredDepartmentFunction)
admin.site.register(PreferredJobTitle)
admin.site.register(Job_Preferences)
admin.site.register(Skills)
admin.site.register(Projects)
admin.site.register(PersonDetails)
admin.site.register(Languange)
admin.site.register(Language_Page)
admin.site.register(Email_Push_Notifications)
admin.site.register(Account_settings)