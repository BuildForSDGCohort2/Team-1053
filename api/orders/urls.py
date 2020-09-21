from django.urls import include, path
from rest_framework import routers
from .views import OrderItemViewSet, OrderViewSet, order_history

router = routers.DefaultRouter()
router.register(r'order-items', OrderItemViewSet)
router.register(r'orders', OrderViewSet, basename='order')

# Wire up our API using automatic URL routing.
# Additionally, we include product, stock and tag URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('order-history/<orderId>', order_history, name='history')
]
