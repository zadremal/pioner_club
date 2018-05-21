from . import models
from rest_framework import serializers

class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Places

        fields = '__all__'

class PartyDetailSerializer(serializers.ModelSerializer):
    place = PlacesSerializer()
    class Meta:
        model = models.Party

        fields = '__all__'



class PartiesListSerializer(serializers.ModelSerializer):

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

class DealsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deals

        fields = (
            "id",
            "name",
            "poster",
            "poster_alt"
        )

class DealDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Deals

        fields = '__all__'
