from django.shortcuts import render
from planetdiscovery.models import PlanetDiscovery
from rest_framework.response import Response
from rest_framework.views import APIView
from planetdiscovery.serializers import PlanetDiscoverySerializer

# Create your views here.
class PlanetDiscoveryCreateView(APIView):
    def get(self, request):
        planetclass = PlanetDiscovery.objects.all()
        serializer = PlanetDiscoverySerializer(planetclass, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanetDiscoverySerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=201)
        return Response(serializer.errors, 
                        status=400)
