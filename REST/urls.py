from django.urls import path
from . import views

urlpatterns = [
    path('parties/<int:pk>/', views.DetailParty.as_view(), name='party_detail'),
    path('parties/', views.ListParties.as_view(), name='parties_list'),
    path('places/', views.ListPlaces.as_view(), name='places_list'),
    path('parties-main/', views.ListPartiesMain.as_view(), name='parties_list_main'),
    path('deals/<int:pk>/', views.DetailDeal.as_view(), name='deal_detail'),
    path('deals/', views.ListDeals.as_view(), name='deals_list'),
    path('deals-main/', views.ListDealsMain.as_view(), name='deals_list_main'),
    path('menu/<int:pk>/', views.MenuSubCategoryList.as_view(), name='category_list'),
    path('menu/', views.MenuList.as_view(), name='menu_list'),
    path('submit/lead/', views.lead_submit, name='lead_submit'),
    path('submit/birthday/', views.birthday_submit, name='birthday_submit'),
    path('submit/banket/', views.banket_submit, name='banket_submit'),
    path('submit/feedback/', views.feedback_submit, name='feedback_submit'),
]
