from rest_framework.authentication import (
    TokenAuthentication, BasicAuthentication
)
from rest_framework.parsers import FileUploadParser
from rest_framework.permissions import IsAuthenticated
from .models import Customer, User
from rest_framework import viewsets
from .serializers import CustomerSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    parser_classes = [FileUploadParser]
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # def put(self, request):
    #     file_obj = request.data['profile_pis']
    #     print(file_obj)


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows customers to be viewed or edited.
    """
    queryset = Customer.objects.all().order_by('-created_at')
    serializer_class = CustomerSerializer
    authentication_classes = [TokenAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
