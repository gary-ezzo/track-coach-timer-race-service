from django.urls import path
from race_service_app.api.views import RaceListAPIView, RaceDetailAPIView

urlpatterns = [
    path('list/', RaceListAPIView.as_view(), name='race-list'),
    path('<int:pk>', RaceDetailAPIView.as_view(), name='race-detail'),
]