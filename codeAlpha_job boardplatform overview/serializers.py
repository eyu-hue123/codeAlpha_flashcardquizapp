from rest_framework import serializers
from .models import Job, Candidate, Application

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = 'all'

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = 'all'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = 'all'