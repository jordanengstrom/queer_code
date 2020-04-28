from rest_framework import routers
from communities.api.views import CommunityViewSet

router = routers.DefaultRouter()
router.register(r'communities/', CommunityViewSet)
