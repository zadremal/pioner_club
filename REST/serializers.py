from . import models
from rest_framework import serializers

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Places

        fields = (
            'name',
            'location',
            'price'
        )

class PartyDetailSerializer(serializers.ModelSerializer):
    place = PlacesSerializer()
    class Meta:
        model = models.Party

        fields = (
            'id',
            'name',
            'date',
            'time_start',
            'time_end',
            'description',
            'place',
            'active',
            'on_main',
            'poster',
            'poster_alt'
        )

class PartyListSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Party

        fields = (
            'id',
            'name',
            'date',
            'description',
            'place',
            'poster',
            'poster_alt'
        )
