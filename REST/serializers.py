from . import models
from rest_framework import serializers

class PartySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Party

        fields = (
            'name',
            'date',
            'time_start',
            'time_end',
            'description',
            'type',
            'active',
            'on_main',
            'poster',
            'poster_alt'
        )


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Places

        fields = (
            'name',
            'location',
            'price'
        )