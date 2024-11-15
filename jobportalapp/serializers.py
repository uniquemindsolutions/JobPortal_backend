from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

# class RegisterSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(
#         required=True,
#         validators=[UniqueValidator(queryset=User.objects.all())]
#     )
#     password = serializers.CharField(
#         write_only=True,
#         required=True,
#         style={'input_type': 'password'}
#     )
#     role = serializers.ChoiceField(choices=User.ROLE_CHOICES,required=True)

#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password', 'role']

#     def create(self, validated_data):
#         user = User(
#             username=validated_data['username'],
#             email=validated_data['email'],
#             role=validated_data['role'],
#             is_active=True  # Set to True for testing
#         )
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, required=True)  # Make sure to include this

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],  # Ensure the role is being set
            is_active=True  # Ensure the user is active upon registration
        )
        user.set_password(validated_data['password'])  # Hash the password
        user.save()
        return user

class TotalVisitorCountSerializer(serializers.ModelSerializer):
    visitor_count = serializers.CharField()  # Accept as string initially

    class Meta:
        model = TotalVisitorCount
        fields = "__all__"

    def validate_visitor_count(self, value):
        """Convert 'k' values to integers."""
        if isinstance(value, str):
            if 'k' in value:
                try:
                    # Convert to float and multiply by 1000
                    return int(float(value.replace('k', '').strip()) * 1000)
                except ValueError:
                    raise serializers.ValidationError("Invalid format for visitor count.")
            else:
                try:
                    return int(value)  # Direct conversion to int
                except ValueError:
                    raise serializers.ValidationError("A valid integer is required.")
        raise serializers.ValidationError("A valid integer is required.")
    
class Shortlisted_CandidatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shortlisted_Candidates
        fields = "__all__"

class Profile_ViewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfileViews
        fields =  "__all__"

    def validate_visitor_count(self, value):
        # Convert 'k' values to integers
        if isinstance(value, str):
            if 'k' in value:
                try:
                    value = float(value.replace('k', '')) * 1000
                except ValueError:
                    raise serializers.ValidationError("Invalid format for visitor count.")
            else:
                try:
                    value = int(value)
                except ValueError:
                    raise serializers.ValidationError("A valid integer is required.")
        return value

class AppliedjobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppliedJobs
        fields = "__all__"

class JobViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobView
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
class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = "__all__"


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"

class MyprofileSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to specify the foreign keys using their IDs
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())
    industry = serializers.PrimaryKeyRelatedField(queryset=Industry.objects.all())  # Only returns ID
    functional_area = serializers.PrimaryKeyRelatedField(queryset=JobCategory.objects.all())  # Only returns ID

    class Meta:
        model = MyProfile
        fields = "__all__"

class NullablePrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def to_internal_value(self, data):
        if data == '':
            return None  # Convert empty string to None
        return super().to_internal_value(data)

class SubmitjobSerializer(serializers.ModelSerializer):
    # industry_name = serializers.StringRelatedField(source='industry', read_only=True)
    industry = serializers.PrimaryKeyRelatedField(queryset=Industry.objects.all())
    job_category = serializers.PrimaryKeyRelatedField(queryset=JobCategory.objects.all())  # Only returns ID
    intermediate = NullablePrimaryKeyRelatedField(queryset=Intermediate.objects.all(), required=False, allow_null=True)
    ug_course = NullablePrimaryKeyRelatedField(queryset=UG.objects.all(), required=False, allow_null=True)
    pg_course = NullablePrimaryKeyRelatedField(queryset=PG.objects.all(), required=False, allow_null=True)

    class Meta:
        model = SubmitJob
        fields = "__all__"
        extra_kwargs = {
            'intermediate': {'required': False, 'allow_null': True},
            'ug_course': {'required': False, 'allow_null': True},
            'pg_course': {'required': False, 'allow_null': True},
        }
    def to_internal_value(self, data):
        # Convert empty strings to None for specific fields
        for field in ['intermediate', 'ug_course', 'pg_course']:
            if data.get(field) == '':
                data[field] = None
        return super().to_internal_value(data)
    
class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account_settings
        fields = "__all__"

class ChangepasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangePassword
        fields = "__all__"
    def validate(self, data):
        """
        Check that the new_password and confirm_password fields match.
        """
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("New password and confirm password do not match.")
        return data

class IntermediateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intermediate  # Make sure the model name is capitalized if needed
        fields = "__all__"

class UGSerializer(serializers.ModelSerializer):
    class Meta:
        model = UG 
        fields = "__all__"

class PGSerializer(serializers.ModelSerializer):
    class Meta:
        model = PG 
        fields = "__all__"

class Email_Push_NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email_Push_Notifications
        fields = "__all__"
        