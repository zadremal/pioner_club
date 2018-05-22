from django.shortcuts import render

# Create your views here.

from rest_framework import generics

from . import models
from . import serializers

class ListParties(generics.ListAPIView):
    queryset = models.Party.objects.all()
    serializer_class = serializers.PartiesListSerializer

class ListPartiesMain(generics.ListAPIView):
    queryset = models.Party.objects.filter(on_main = True, active=True)
    serializer_class = serializers.PartiesListSerializer



class DetailParty(generics.RetrieveAPIView):
    queryset = models.Party.objects.all()
    serializer_class = serializers.PartyDetailSerializer


class ListDeals(generics.ListAPIView):
    queryset = models.Deals.objects.all()
    serializer_class = serializers.DealsListSerializer


class ListDealsMain(generics.ListAPIView):
    queryset = models.Deals.objects.filter(on_main = True)
    serializer_class = serializers.DealsListSerializer

class DetailDeal(generics.RetrieveAPIView):
    queryset = models.Deals.objects.all()
    serializer_class = serializers.DealDetailSerializer

class MenuSubCategoryList(generics.ListAPIView):
    serializer_class = serializers.MenuCategorySerializer

    def get_queryset(self):
        return models.DishCategories.objects.filter(menu_category = self.kwargs['pk'])


class MenuList(generics.ListAPIView):
    queryset = models.MenuCategories.objects.all()
    serializer_class = serializers.MenuSerializer