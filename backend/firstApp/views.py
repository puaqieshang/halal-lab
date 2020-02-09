from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets          # add this
from .serializers import firstAppSerializer      # add this
from .models import firstApp                     # add this
        
class firstAppView(viewsets.ModelViewSet):       # add this
	serializer_class = firstAppSerializer          # add this
	queryset = firstApp.objects.all()              # add this
