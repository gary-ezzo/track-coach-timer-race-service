from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
import firebase_admin
from firebase_admin import credentials, auth

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        # auth_token = request.META.get('HTTP_AUTHORIZATION')
        # cred = credentials.Certificate("/workspaces/python/track-coach-timer-race-service/credentials.json")
        
        # try:
        #     firebase_admin.initialize_app(cred)
        # except:
        #     print('thats ok')
        
        # decoded_token = auth.verify_id_token(auth_token)
        
        return None