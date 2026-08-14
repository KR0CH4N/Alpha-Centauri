from django.shortcuts import render
from roles.models import Role
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from roles.serializers import RolesSerializer

# Create your views here.
class RolesCreateView(APIView):
    def get(self, request):
        roles = Role.objects.all()
        serializer = RolesSerializer(roles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RolesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=201)
        return Response(
            {'message': 'Invalid'},
                        status=400)
