from planetclass.models import PlanetClass
from rest_framework import serializers

class PlanetClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetClass

        fields = '__all__'