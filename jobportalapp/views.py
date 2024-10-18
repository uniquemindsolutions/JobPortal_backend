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
from rest_framework.response import Response
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes,force_str
from .utils import account_activation_token

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Save the new user
            user.is_active = False  # Deactivate account until email confirmed
            user.save()

            # Send confirmation email
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            activation_link = reverse('activate', kwargs={'uidb64': uid, 'token': token})
            activation_url = f'http://{current_site.domain}{activation_link}'

            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': uid,
                'token': token,
                'activation_url': activation_url
            })
            send_mail(mail_subject, message, 'your-email@gmail.com', [user.email])

            return Response({"message": "User registered successfully. Please check your email to activate your account."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ActivateAccountView(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response({"message": "Account activated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Activation link is invalid!"}, status=status.HTTP_400_BAD_REQUEST)
    
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
    queryset = AppliedJobs.objects.all()
    serializer_class = AppliedjobsSerializer

class JobViewViewSet(viewsets.ModelViewSet):
    queryset = JobView.objects.all()
    serializer_class = JobViewSerializer

class MyprofileViewSet(viewsets.ModelViewSet):
    queryset = MyProfile.objects.all()
    serializer_class = MyprofileSerializer

    # Override the create method if needed for additional logic
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        # Modify the response to include a success message
        response.data['message'] = 'Profile created successfully!'
        return Response(response.data, status=status.HTTP_201_CREATED)

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

# For filtering states by country_id
class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        country_id = self.request.query_params.get('countryid', None)
        if country_id:
            queryset = queryset.filter(country__id=country_id)
        return queryset


# For filtering cities by state_id
class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        state_id = self.request.query_params.get('stateid', None)
        if state_id:
            queryset = queryset.filter(state__id=state_id)
        return queryset

class JobCategoryViewSet(viewsets.ModelViewSet):
    queryset = JobCategory.objects.all()
    serializer_class = JobCategorySerializer

# ViewSet for Industry
class IndustryViewSet(viewsets.ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

class Submitjobviewset(viewsets.ModelViewSet):
    queryset = SubmitJob.objects.all()
    serializer_class = SubmitjobSerializer 

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data['message'] = 'Job submitted successfully!'
        return Response(response.data, status=status.HTTP_201_CREATED)
    
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
    
class IntermediateViewSet(viewsets.ModelViewSet):
    queryset = Intermediate.objects.all()
    serializer_class = IntermediateSerializer

class UGViewet(viewsets.ModelViewSet):
    queryset = UG.objects.all()
    serializer_class = UGSerializer

class PGViewset(viewsets.ModelViewSet):
    queryset = PG.objects.all()
    serializer_class = PGSerializer 

