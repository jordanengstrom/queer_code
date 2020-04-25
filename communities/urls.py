from django.urls import path
from .views import (
    CommunityListView,
    CommunityCreateView,
    CommunityUpdateView,
    CommunityDeleteView
)


url_patterns = [
    path('/communities', CommunityListView.as_view(), name='communities-home'),
    path()
]
