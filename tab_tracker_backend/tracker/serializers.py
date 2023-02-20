from rest_framework import serializers
from .models import *



class NewTabSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTab
        fields = '__all__'


class SwitchTabSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SwitchTab
        fields = '__all__'
