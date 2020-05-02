from rest_framework import routers
from communities.api.views import CommunityViewSet
from articles.api.views import ArticleViewSet
from core.views import IndexTemplateView

router = routers.DefaultRouter()
router.register(r'communities', CommunityViewSet)
router.register(r'articles', ArticleViewSet)
