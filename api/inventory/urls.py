from django.urls import include, path
from rest_framework import routers
from .views import ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include product URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls))
]
