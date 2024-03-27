from django.urls import path
# from race_service_app.api.views import race_list, race_details
from race_service_app.api.views import RaceListAPIView, RaceDetailAPIView

urlpatterns = [
    # path('list/', race_list, name='race-list'),
    # path('<int:pk>', race_details, name='race-detail'),
    path('list/', RaceListAPIView.as_view(), name='race-list'),
    path('<int:pk>', RaceDetailAPIView.as_view(), name='race-detail'),
]