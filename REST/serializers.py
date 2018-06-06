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

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dish
        fields = "__all__"


class MenuCategorySerializer(serializers.ModelSerializer):
    dish= DishSerializer(many=True, read_only=True)
    class Meta :

        model = models.DishCategories
        fields = (
            'id',
            'menu_category',
            'dish_category',
            'dish',
            'dish_category_description',
        )


class MenuSerializer(serializers.ModelSerializer):
    sub_category = MenuCategorySerializer(many=True, read_only=True)
    class Meta:
        model = models.MenuCategories
        fields = (
            "id",
            "name",
            "sub_category"
        )

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Leads
        fields = "__all__"

class BirthdaySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Birthdays
        fields = "__all__"

class BanketSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Bankets
        fields = "__all__"