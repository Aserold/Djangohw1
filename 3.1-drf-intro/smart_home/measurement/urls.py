from django.urls import path
from .views import SensorListCreateView, SensorRetrieveUpdateView, TemperatureMeasurementCreateView, SensorDetailView

urlpatterns = [
    path('sensors/', SensorListCreateView.as_view()),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view()),
    path('sensors/<int:pk>/', SensorDetailView.as_view(), name='sensor-detail'),
    path('measurements/', TemperatureMeasurementCreateView.as_view()),
]