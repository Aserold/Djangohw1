from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, RetrieveAPIView
from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, MeasurementSerializer, SensorListSerializer


class SensorListCreateView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorListSerializer


class SensorRetrieveUpdateView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class TemperatureMeasurementCreateView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
