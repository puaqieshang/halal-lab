# todo/serializers.py

from rest_framework import serializers
from .models import firstApp
      
class firstAppSerializer(serializers.ModelSerializer):
	class Meta:
		model = firstApp
		fields = ('id', 'title', 'description', 'halal')
