# from django.contrib.auth import get_user_model
# from django.contrib.auth.backends import ModelBackend

# User = get_user_model()  # This will get your custom user model

# class EmailBackend(ModelBackend):
#     def authenticate(self, request, email=None, password=None, **kwargs):
#         try:
#             user = User.objects.get(email=email)
#         except User.DoesNotExist:
#             return None
#         if user.check_password(password):
#             return user
#         return None
# jobportalapp/auth_backends.py

from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
