from django.shortcuts import render
from roles.models import Role
from rest_framework.response import Response
from rest_framework.views import APIView
from roles.serializers import RolesSerializer

# Create your views here.
class RolesCreateView(APIView):
    def get(self, request):
        planetclass = Role.objects.all()
        serializer = RolesSerializer(planetclass, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RolesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=201)
        return Response(serializer.errors, 
                        status=400)
