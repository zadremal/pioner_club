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
    dish = DishSerializer(many=True, read_only=True)

    class Meta:
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


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Countries
        fields = "__all__"

class BeerSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=False)

    class Meta:
        model = models.Beer
        fields = (
            "id",
            "name",
            "details",
            "alcohol",
            "country",
            "price03",
            "price05",
        )


class BottleBeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BottleBeer
        fields = "__all__"


class BottleCountrySerializer(serializers.ModelSerializer):
    bottle_beer = BottleBeerSerializer(many=True, read_only=True)

    class Meta:
        model = models.Countries
        fields = (
            "id",
            "name",
            "bottle_beer"
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


class FeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Feedbacks
        fields = "__all__"
