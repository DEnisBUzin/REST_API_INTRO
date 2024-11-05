from django.urls import path

from measurement.views import AllSensorsView, SensorView, MeasurementView

urlpatterns = [
    path('sensors/', AllSensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementView.as_view())
]
