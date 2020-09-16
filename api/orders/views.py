from .models import OrderItem, Order, Tracking
from rest_framework import viewsets
from rest_framework.authentication import (
    TokenAuthentication, BasicAuthentication
)
from rest_framework.permissions import IsAuthenticated
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
    queryset = OrderItem.objects.filter(is_ordered=False).order_by('-id')
    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tag to be viewed or edited.
    """
    queryset = Order.objects.filter().order_by('-date_created')
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order_items = self.request.data.get('order_items')
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(
            customer=customer, order_id=generate_id(), items=order_items
        )


class TrackingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Tracking.objects.all().order_by('-id')
    serializer_class = TrackingSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
