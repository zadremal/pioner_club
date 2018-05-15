from django.conf.urls import url

from . import views

urlpatterns =  [
    url(r'^$', views.PartiesList.as_view(), name='parties_list'),

]