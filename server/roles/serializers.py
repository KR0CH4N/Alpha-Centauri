from roles.models import Role
from rest_framework import serializers

class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role

        fields = '__all__'