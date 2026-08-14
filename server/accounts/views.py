from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from accounts.models import Account
from accounts.serializers import AccountSerializer

# Create your views here.

class AccountListCreateView(APIView):
    def get(self, request):
        accounts = Account.objects.all()
        serializer = AccountSerializer(accounts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, 
                            status=201)
        return Response({
            'message': 'Invalid'
        }, 
                        status=400)

