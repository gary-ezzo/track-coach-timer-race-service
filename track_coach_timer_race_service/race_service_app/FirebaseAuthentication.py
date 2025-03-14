from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
import firebase_admin
from firebase_admin import credentials, auth

class FirebaseAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        auth_token = request.data.get('authToken')
        cred = credentials.Certificate("/workspaces/track-coach-timer-dev-environment/track-coach-timer-race-service/credentials.json")
        
        if firebase_admin._apps == {}:
            firebase_admin.initialize_app(cred)
        
        decoded_token = auth.verify_id_token(auth_token)
        
        return None