from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','nombre','email','nombreCorto','categoria','nivelSni','orcId','arxivId']

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            nombre = validated_data['nombre']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        