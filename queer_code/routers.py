from rest_framework import routers
from communities.views import *


router = routers.DefaultRouter()
router.register(r'/communities', CommunityListView)
