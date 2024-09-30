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
        model = Appliedjobs
        fields = "__all__"

class JobViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobView
        fields = "__all__"

class MyprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myprofile
        fields = "__all__"

class NewjobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newjob
        fields = "__all__"
class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountSettings
        fields = "__all__"
class ChangepasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Changepassword
        fields = "__all__"