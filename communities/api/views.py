from rest_framework import viewsets, renderers
from communities.models import Community
from .serializers import CommunitySerializer


class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer
