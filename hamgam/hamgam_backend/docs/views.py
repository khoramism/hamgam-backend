from django.shortcuts import render
from .serializers import DocSerializer
# Create your views here.
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import status, filters , views 
from rest_framework import generics
from .models import Doc 
from .serializers import DocSerializer


class DocListView(generics.ListAPIView):
    queryset = Doc.objects.filter(active=True)
    serializer_class = DocSerializer


class DocDetailView(generics.RetrieveAPIView):
    queryset = Doc.objects.filter(active=True)
    serializer_class = DocSerializer
