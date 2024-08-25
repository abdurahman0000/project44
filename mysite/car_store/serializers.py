from rest_framework import serializers
from .models import *

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class MarkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'