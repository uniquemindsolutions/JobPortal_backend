from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import *
# User Serializer
# Register Serializer
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CustomUser  # Use CustomUser, not User
#         fields = ('username', 'email', 'password', 'user_type')

#     def create(self, validated_data):
#         user = CustomUser(**validated_data)  # Create an instance of CustomUser
#         user.set_password(validated_data['password'])  # Hash the password
#         user.save()
#         return user

# # Login Serializer
# class LoginSerializer(serializers.Serializer):
#     username = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         user = authenticate(**data)
#         if user and user.is_active:
#             return user
#         raise serializers.ValidationError("Invalid credentials")

class AppliedJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliedjobs
        fields = "__all__"


class JobalertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobalerts
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"

class ShortlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortlist
        fields = "__all__"

class UserChangepasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserChangePassword
        fields = "__all__"

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields =  "__all__"

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields =  "__all__"

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields =  "__all__"

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields =  "__all__"

class WorkexperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workexperience
        fields =  "__all__" 

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields =  "__all__"

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields =  "__all__"

class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institute
        fields = "__all__"

class Education_DetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education_Details
        fields =  "__all__"
    
    def validate_passing_year(self, value):
        # Check if value is a valid integer
        if not isinstance(value, int):
            raise serializers.ValidationError("Passing year must be an integer.")
        return value

class PreferredDepartmentFunctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferredDepartmentFunction
        fields =  "__all__"

class PreferredJobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PreferredJobTitle
        fields = "__all__"

class Job_PreferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Preferences
        fields = "__all__"

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields =  "__all__"

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"

class PersonDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonDetails
        fields =  "__all__"

class LanguangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languange
        fields =  "__all__"

class Language_PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language_Page
        fields =  "__all__"

class Email_Push_NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email_Push_Notifications
        fields =  "__all__"

class Account_settingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_settings
        fields =  "__all__"

class SavedJobsSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source='user.id')
    job_id = serializers.IntegerField(source='job.id')

    class Meta:
        model = SavedJobs
        fields = ['user_id', 'job_id']