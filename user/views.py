from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework import viewsets
from rest_framework import status
import requests
from datetime import datetime

# Register API
# class RegisterAPI(generics.GenericAPIView):
#     serializer_class = RegisterSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.save()  # Ensure this is a CustomUser instance

#         # Debugging: Check the type of user
#         print(type(user))  # This should show <class 'user.models.CustomUser'>
#         print(user)  # Print the user object to ensure it's the instance, not a string

#         # Ensure you are creating the token for the CustomUser instance
#         token, created = Token.objects.get_or_create(user=user)
        
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": token.key
#         })
    
# # Login API
# class LoginAPI(generics.GenericAPIView):
#     serializer_class = LoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             "user": UserSerializer(user, context=self.get_serializer_context()).data,
#             "token": token.key
#         })

# # Get User Profile
# class UserProfileAPI(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = UserSerializer

#     def get_object(self):
#         return self.request.user


class AppliedjobsViewSet(viewsets.ModelViewSet):
    queryset = Appliedjobs.objects.all()
    serializer_class = AppliedJobSerializer

class JobalertViewSet(viewsets.ModelViewSet):
    queryset = Jobalerts.objects.all()
    serializer_class = JobalertsSerializer

class MessageViewset(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class ShortlistViewSet(viewsets.ModelViewSet):
    queryset = Shortlist.objects.all()
    serializer_class = ShortlistSerializer

class SubmitJobView(APIView):
    def get(self, request):
        admin_api_url = 'http://127.0.0.1:8000/submitnewjob/'  # Adjust this URL accordingly

        # Forward the request data to the admin API (if there are query parameters)
        response = requests.get(admin_api_url, params=request.query_params)
        # Check if the response is JSON
        if response.headers.get('Content-Type') == 'application/json':
            try:
                response_data = response.json()
                return Response(response_data, status=response.status_code)
            except ValueError as e:
                return Response({"error": "Failed to parse JSON response."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response({"error": "Expected JSON response, got something else."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class UserChangePasswordView(generics.UpdateAPIView):
    serializer_class = UserChangepasswordSerializer
    model = UserChangePassword

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

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class WorkexperienceViewSet(viewsets.ModelViewSet):
    queryset = Workexperience.objects.all()
    serializer_class = WorkexperienceSerializer

class QualificationViewSet(viewsets.ModelViewSet):
    queryset = Qualification.objects.all()
    serializer_class = QualificationSerializer

class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer

class InstituteViewSet(viewsets.ModelViewSet):
    queryset = Institute.objects.all()
    serializer_class = InstituteSerializer


class Education_DetailsViewSet(viewsets.ModelViewSet):
    queryset = Education_Details.objects.all()
    serializer_class = Education_DetailsSerializer

    def perform_create(self, serializer):
        passing_year = self.request.data.get('passing_year')
        if isinstance(passing_year, str):  # Check if it’s a string
            passing_year = int(passing_year)  # Convert to int
        serializer.save(passing_year=passing_year)

class PreferredDepartmentFunctionViewSet(viewsets.ModelViewSet):
    queryset = PreferredDepartmentFunction.objects.all()
    serializer_class = PreferredDepartmentFunctionSerializer

class PreferredJobTitleViewSet(viewsets.ModelViewSet):
    queryset = PreferredJobTitle.objects.all()
    serializer_class = PreferredJobTitleSerializer

class JobPreferencesViewSet(viewsets.ModelViewSet):
    queryset = Job_Preferences.objects.all()
    serializer_class = Job_PreferencesSerializer

class SkillsViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

class PersonDetailsViewSet(viewsets.ModelViewSet):
    queryset = PersonDetails.objects.all()
    serializer_class = PersonDetailsSerializer

class PersonDetailsByIdView(APIView):
    def post(self, request, *args, **kwargs):
        person_id = request.data.get('id')  # Retrieve the 'id' from the POST data

        if person_id:
            try:
                # Retrieve the PersonDetails object by id
                person = PersonDetails.objects.get(id=person_id)
                serializer = PersonDetailsSerializer(person)
                # Return the serialized data
                return Response(serializer.data, status=status.HTTP_200_OK)
            except PersonDetails.DoesNotExist:
                return Response({'error': 'Person not found'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'error': 'ID is required'}, status=status.HTTP_400_BAD_REQUEST)

class LanguangeViewSet(viewsets.ModelViewSet):
    queryset = Languange.objects.all()
    serializer_class = LanguangeSerializer

class LanguagePageViewSet(viewsets.ModelViewSet):
    queryset = Language_Page.objects.all()
    serializer_class = Language_PageSerializer

class Email_Push_NotificationsViewSet(viewsets.ModelViewSet):
    queryset = Email_Push_Notifications.objects.all()
    serializer_class = Email_Push_NotificationsSerializer

class Account_settingsViewSet(viewsets.ModelViewSet):
    queryset = Account_settings.objects.all()
    serializer_class = Account_settingsSerializer

class SavedJobsView(APIView): 
    def post(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_403_FORBIDDEN)

        user = request.user
        job_id = request.data.get('job_id')

        # Check if job_id is provided
        if not job_id:
            return Response({"error": "Job ID is required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the job exists
        try:
            job = SubmitJob.objects.get(id=job_id)  # Ensure you're querying the SubmitJob model
        except SubmitJob.DoesNotExist:
            return Response({"error": "Job not found"}, status=status.HTTP_404_NOT_FOUND)

        # Check if the job is already saved by the user
        if SavedJobs.objects.filter(user_id=user, job_id=job).exists():
            return Response({"message": "Job already saved"}, status=status.HTTP_200_OK)

        # Save the job for the user
        saved_job = SavedJobs.objects.create(user_id=user, job_id=job)
        serializer = SavedJobsSerializer(saved_job)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request):
        # Check if user is authenticated
        if not request.user.is_authenticated:
            return Response({"error": "Authentication required"}, status=status.HTTP_403_FORBIDDEN)

        user = request.user
        submitted_jobs = SavedJobs.objects.filter(user_id=user)  # Use 'user_id' to filter
        serializer = SavedJobsSerializer(submitted_jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)