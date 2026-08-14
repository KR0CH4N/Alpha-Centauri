from django.shortcuts import render
from planetclass.models import PlanetClass
from rest_framework.response import Response
from rest_framework.views import APIView
from planetclass.serializers import PlanetClassSerializer

# Create your views here.
class PlanetClassCreateView(APIView):
    def get(self, request):
        planetclass = PlanetClass.objects.all()
        serializer = PlanetClassSerializer(planetclass, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PlanetClassSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=201)
        return Response({
            'message', 'Invalid'
        }, 
                        status=400)

