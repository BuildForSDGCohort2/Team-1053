from rest_framework.authentication import (
    TokenAuthentication, BasicAuthentication
)
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Customer, User
from rest_framework import viewsets
from .serializers import CustomerSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    lookup_field = 'user'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True)
    def user(self, request, pk=None):
        # pk will be the user id
        queryset = Customer.objects.get(user=pk)
        serializer = CustomerSerializer(queryset, many=True)
        return Response(serializer.data)
