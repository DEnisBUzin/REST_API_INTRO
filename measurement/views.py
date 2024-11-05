# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateAPIView, ListCreateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailInformSerializer


class AllSensorsView(ListCreateAPIView):
    """ Класс для реализации:
    GET - просматривать данные
    POST - записывать новые данные """

    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def perform_create(self, serializer):
        serializer.save()
        return Response({'status', 'post - success'})


class SensorView(RetrieveUpdateAPIView):
    """ Класс для реализации GET и PATCH запросов,
     здесь сможем как просматривать детальную информацию,
      так и частично обновлять сенсоры """

    queryset = Sensor.objects.all()
    serializer_class = None

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return SensorDetailInformSerializer
        elif self.request.method == 'PATCH':
            return SensorSerializer

    # def perform_update(self, serializer):
    #     serializer.save()


class MeasurementView(CreateAPIView):
    """Класс для добавления измерения"""
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


