from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'Appliedjobs',AppliedjobsViewSet,basename='Appliedjobs'),
router.register(r'jobalerts',JobalertViewSet,basename='Jobalerts'),
router.register(r'messages',MessageViewset,basename='Messages'),
router.register(r'shortlist',ShortlistViewSet,basename='Shortlist'),
router.register(r'Countries',CountryViewSet,basename='Countries'),
router.register(r'States',StateViewSet,basename='States'),
router.register(r'Cities',CityViewSet,basename='Cities'),
router.register(r'Userprofile',UserProfileViewSet,basename='Userprofile'),
router.register(r'Workexperience',WorkexperienceViewSet,basename='Workexperience'),
router.register(r'Qualification',QualificationViewSet,basename='Qualification'),
router.register(r'Specialization',SpecializationViewSet,basename='Specialization'),
router.register(r'Institute',InstituteViewSet,basename='Institute'),
router.register(r'EducationDetails',Education_DetailsViewSet,basename='EducationDetails'),
router.register(r'PreferredDepartmentFunction',PreferredDepartmentFunctionViewSet,basename='PreferredDepartmentFunction'),
router.register(r'PreferredJobTitle',PreferredJobTitleViewSet,basename='PreferredJobTitle'),
router.register(r'JobPreferences',JobPreferencesViewSet,basename='JobPreferences'),
router.register(r'Skills',SkillsViewSet,basename='Skills'),
router.register(r'Projects',ProjectsViewSet,basename='Projects'),
router.register(r'PersonDetails',PersonDetailsViewSet,basename='PersonDetails'),
router.register(r'Languange',LanguangeViewSet,basename='Languange'),
router.register(r'LanguagePage',LanguagePageViewSet,basename='LanguagePage'),
router.register(r'Emailpushnotification',Email_Push_NotificationsViewSet,basename='Emailpushnotification'),
router.register(r'Accountsetting',Account_settingsViewSet,basename='Accountsetting'),

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('profile/', UserProfileAPI.as_view(), name='profile'),
    path('change_password/', UserChangePasswordView.as_view(), name='change_password'),
    path('submit-job/', SubmitJobView.as_view(), name='submit-job')
]
