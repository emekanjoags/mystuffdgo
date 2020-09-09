from rest_framework import serializers

from .models import BioData

class BioDataSerializer(serializers.ModelSerializer):
    model = BioData
    fields = '__all__'
