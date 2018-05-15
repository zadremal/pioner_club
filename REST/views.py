from django.shortcuts import render

# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from . import models
from . import serializers


class PartiesList(APIView):
    def get(self, request, format=None):
        parties = models.Party.objects.all()
        serializer = serializers.PartySerializer(parties, many=True)
        return Response(serializer.data)