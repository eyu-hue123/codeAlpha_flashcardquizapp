from rest_framework import serializers
from .models import Event, Registration

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = 'all'

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = 'all'
