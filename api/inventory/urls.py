from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet, StockViewSet, TagViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'stock', StockViewSet)
router.register(r'tags', TagViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include product, stock and tag URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
