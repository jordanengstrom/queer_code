from django.urls import path
from .views import (
    CommunityListView,
    CommunityCreateView,
    CommunityUpdateView,
    CommunityDeleteView
)


url_patterns = [
    path('', CommunityListView.as_view()),
    path('create/', CommunityCreateView.as_view()),
    path('<pk>/', CommunityDetailView.as_view()),
    path('<pk>/update/', CommunityUpdateView.as_view()),
    path('<pk>/delete/', CommunityDestroyView.as_view()),
]
