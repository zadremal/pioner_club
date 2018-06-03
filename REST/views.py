from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .mail_jet import send_mail
from . import models
from . import serializers


class ListParties(generics.ListAPIView):
    queryset = models.Party.objects.all()
    serializer_class = serializers.PartiesListSerializer


class ListPlaces(generics.ListAPIView):
    queryset = models.Places.objects.all()
    serializer_class = serializers.PlacesSerializer


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


@api_view(['POST'])
def lead_submit(request):
    serializer = serializers.LeadSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        send_mail(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)