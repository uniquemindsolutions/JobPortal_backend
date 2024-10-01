from django.urls import path,include
from .views import * 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'totalvistors',Total_Visitor_CountViewSet,basename='totalvisitorcount'),
router.register(r'shortlistedcandidates', Shortlisted_CandidatesViewSet, basename='shortlistedcandidates')
router.register(r'profileview',Profile_ViewsViewSet,basename='profileview'),
router.register(r'appliedjobs',AppliedjobsViewSet,basename='appliedjobs'),
router.register(r'jobviews', JobViewViewSet,basename='jobviews'),
router.register(r'myprofile', MyprofileViewSet,basename='Myprofile'),
router.register(r'countries', CountryViewSet,basename='countries'),
router.register(r'states', StateViewSet,basename='states'),
router.register(r'cities', CityViewSet,basename='cities'),
router.register(r'myprofile',MyprofileViewSet,basename='myprofileview'),
router.register(r'submitjob',Submitjobviewset,basename='mynewjob'),
router.register(r'accountsettings',AccountSettingsViewSet,basename='accountsettings'),

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]