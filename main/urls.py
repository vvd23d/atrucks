from django.urls import path

from .views import *


urlpatterns = [
    # path('', tels_list, name='tels_list_url'),
    path('', Search.as_view(), name='search_url'),
]
