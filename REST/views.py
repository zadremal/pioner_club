from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from . import models
from . import serializers

class ListParties(generics.ListAPIView):
    queryset = models.Party.objects.all()
    serializer_class = serializers.PartyListSerializer


class DetailParties(generics.RetrieveAPIView):
    queryset = models.Party.objects.all()
    serializer_class = serializers.PartyDetailSerializer