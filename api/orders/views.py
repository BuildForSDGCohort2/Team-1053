from .models import OrderItem, Order, Tracking
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import (
    OrderItemSerializer,
    OrderSerializer,
    TrackingSerializer
)
from .models import Customer
from api.utils.helpers import generate_id


class OrderItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stock to be viewed or edited.
    """
    queryset = OrderItem.objects.all().order_by('-id')
    serializer_class = OrderItemSerializer
    permission_classes = [AllowAny]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tag to be viewed or edited.
    """
    queryset = Order.objects.all().order_by('-date_created')
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(customer=customer, order_id=generate_id())


class TrackingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Tracking.objects.all().order_by('-id')
    serializer_class = TrackingSerializer
