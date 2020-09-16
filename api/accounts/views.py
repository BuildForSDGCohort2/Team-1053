from .models import Customer, User
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomerSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]
