from django.urls import path, include
from apps.cars.api.views import CarListView, CarRetrieveView

app_name = 'car_api'

urlpatterns = [
    path('cars/', CarListView.as_view(), name='car-list'),
    path('cars/<int:pk>/', CarRetrieveView.as_view(), name='car-detail')
]
