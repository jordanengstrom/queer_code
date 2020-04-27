from rest_framework import routers
from communities.views import CommunityViewSet


router = routers.DefaultRouter()
router.register(r'community', CommunityViewSet)
