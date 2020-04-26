from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Community
from .serializers import CommunitySerializer

# can do a Viewset here, but want to practice other ways of doing things


class CommunityListView(ListView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityCreateView(CreateView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityUpdateView(UpdateView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CommunityDeleteView(DeleteView):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
