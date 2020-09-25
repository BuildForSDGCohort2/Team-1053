from .models import OrderItem, Order, Tracking
from rest_framework import viewsets
from rest_framework.authentication import (
    TokenAuthentication, BasicAuthentication
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes
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
    admin_actions = [
        'On Hold', 'Confirmed',
        'Rejected', 'Packed', 'Dispatched',
        'Out for delivery', 'Delivered'
    ]
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order_items = self.request.data.get('order_items')
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(
            customer=customer, order_id=generate_id(), items=order_items
        )

    def get_queryset(self):
        queryset = Order.objects.all().order_by('-date_created')
        if self.request.user.is_staff is False:
            customer = Customer.objects.get(user=self.request.user)
            queryset = Order.objects.filter(
                customer=customer).order_by('-date_created')
        return queryset


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_history(request, orderId):
    try:
        queryset = Tracking.objects.filter(
            order_id=orderId).order_by('-event_date')
        serializer = TrackingSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
@authentication_classes([TokenAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def order_summary(request):
    try:
        queryset = Order.objects.order_by('-event_date')
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)
    except Exception as e:
        print(e)
        return Response(
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
