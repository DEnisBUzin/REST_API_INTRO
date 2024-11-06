from rest_framework import serializers

from measurement.models import Sensor, Measurement


class SensorSerializer(serializers.ModelSerializer):
    """Сериализатор датчиков"""

    class Meta:
        model = Sensor
        fields = ['id',
                  'name',
                  'description'
                  ]


class MeasurementSerializer(serializers.ModelSerializer):
    """ Сериализатор измерений """

    class Meta:
        model = Measurement
        fields = [
            'id',
            'sensor',
            'temperature',
            'created_at',
        ]


class SensorDetailInformSerializer(serializers.ModelSerializer):
    """ Сериализатор детальной информации о сенсорах """

    measurements = MeasurementSerializer(read_only=True,
                                          many=True)

    class Meta:
        model = Sensor
        fields = [
            'id',
            'name',
            'description',
            'measurements'
        ]