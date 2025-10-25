from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    first_name = serializers.CharField(max_length=40)
    last_name = serializers.CharField(max_length=40)
    email = serializers.EmailField()
    phone = serializers.CharField(max_length=11)

    def create(self, validated_data):
        return Customer.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance
