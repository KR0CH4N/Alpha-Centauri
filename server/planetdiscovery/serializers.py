from planetdiscovery.models import PlanetDiscovery
from rest_framework import serializers


class PlanetDiscoverySerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanetDiscovery

        fields = '__all__'