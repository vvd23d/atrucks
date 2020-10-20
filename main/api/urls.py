from django.urls import path
from django.urls import re_path

from .views import (
    NumberingListView,
    # ArticleDetailView,
    # ArticleCreateView,
    # ArticleUpdateView,
    # ArticleDeleteView,
    TelAPIView
)


urlpatterns = [
    path('', NumberingListView.as_view()),
    path('<str:tel>/', TelAPIView.as_view()),
]
