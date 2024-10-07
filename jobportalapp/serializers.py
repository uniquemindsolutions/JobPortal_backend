from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password],
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
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
        fields =  ['name']

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields =  ['name','country']

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields =  ['name','state']

class MyprofileSerializer(serializers.ModelSerializer):
    # Use PrimaryKeyRelatedField to specify the foreign keys using their IDs
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())
    state = serializers.PrimaryKeyRelatedField(queryset=State.objects.all())
    city = serializers.PrimaryKeyRelatedField(queryset=City.objects.all())

    class Meta:
        model = MyProfile
        fields = "__all__"

class JobCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = JobCategory
        fields = "__all__"


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = "__all__"

class SubmitjobSerializer(serializers.ModelSerializer):
    industry = IndustrySerializer()  # Nested serializer for industry
    job_category = JobCategorySerializer()  # Nested serializer for jobCategory
    class Meta:
        model = SubmitJob
        fields = "__all__"

    def create(self, validated_data):
        # Extract the nested objects
        industry_data = validated_data.pop('industry')
        job_category_data = validated_data.pop('job_category')

        # Create the industry and job_category instances
        industry, created = Industry.objects.get_or_create(**industry_data)
        job_category, created = JobCategory.objects.get_or_create(**job_category_data)

        # Create the SubmitJob instance
        submit_job = SubmitJob.objects.create(
            industry=industry,
            job_category=job_category,
            **validated_data
        )
        return submit_job

    def update(self, instance, validated_data):
        # Similar logic for updating instances
        industry_data = validated_data.pop('industry', None)
        job_category_data = validated_data.pop('job_category', None)

        if industry_data:
            industry, created = Industry.objects.get_or_create(**industry_data)
            instance.industry = industry

        if job_category_data:
            job_category, created = JobCategory.objects.get_or_create(**job_category_data)
            instance.job_category = job_category

        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSettings
        fields = "__all__"

class ChangepasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChangePassword
        fields = "__all__"

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = "__all__"
        