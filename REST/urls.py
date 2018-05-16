
from django.urls import path

from . import views

urlpatterns =  [
    path('parties/<int:pk>/', views.DetailParties.as_view(), name='parties_detail'),
    path('parties/', views.ListParties.as_view(), name='parties_list'),

]