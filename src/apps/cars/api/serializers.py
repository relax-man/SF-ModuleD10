from rest_framework import serializers
from apps.cars.models import Car


class CarSerializer(serializers.ModelSerializer):
    transmission = serializers.SerializerMethodField()

    def get_transmission(self, obj):
        return obj.get_transmission_display()

    class Meta:
        model = Car
        fields = '__all__'
