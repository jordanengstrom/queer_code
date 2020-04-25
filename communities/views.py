from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Community


class CommunityListView(ListView):
    model = Community
    context_object_name = 'communities'
    ordering = ['name']


class CommunityCreateView(CreateView):
    model = Community
    fields = ['name', 'description']


class CommunityUpdateView(UpdateView):
    model = Community
    fields = ['name', 'description']


class CommunityDeleteView(DeleteView):
    model = Community
    success_url = '/communities'
