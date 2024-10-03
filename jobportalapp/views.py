from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import generics

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Save the new user
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        # We pass email as the username since the custom backend uses it
        user = authenticate(request, username=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid email or password"}, status=status.HTTP_400_BAD_REQUEST)
        
class Total_Visitor_CountViewSet(viewsets.ModelViewSet):
    queryset = TotalVisitorCount.objects.all()
    serializer_class = TotalVisitorCountSerializer

class Shortlisted_CandidatesViewSet(viewsets.ModelViewSet):
    queryset = Shortlisted_Candidates.objects.all()
    serializer_class = Shortlisted_CandidatesSerializer

class Profile_ViewsViewSet(viewsets.ModelViewSet):
    queryset = ProfileViews.objects.all()
    serializer_class = Profile_ViewsSerializer

class AppliedjobsViewSet(viewsets.ModelViewSet):
    queryset = Appliedjobs.objects.all()
    serializer_class = AppliedjobsSerializer

class JobViewViewSet(viewsets.ModelViewSet):
    queryset = JobView.objects.all()
    serializer_class = JobViewSerializer

class MyprofileViewSet(viewsets.ModelViewSet):
    queryset = Myprofile.objects.all()
    serializer_class = MyprofileSerializer

    # Override the create method if needed for additional logic
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class Submitjobviewset(viewsets.ModelViewSet):
    queryset = Submitjob.objects.all()
    serializer_class = SubmitjobSerializer 

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
class AccountSettingsViewSet(viewsets.ModelViewSet):
    queryset = AccountSettings.objects.all()
    serializer_class = AccountSettingsSerializer

class ChangePasswordView(generics.UpdateAPIView):
    serializer_class = ChangepasswordSerializer
    model = User

    def get_object(self, queryset=None):
        return self.request.user

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Save the new password
            serializer.save()
            return Response({"detail": "Password has been changed successfully."}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    