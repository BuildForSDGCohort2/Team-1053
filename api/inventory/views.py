from .models import Stock, Tag, Product
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .serializers import (
    StockSerializer,
    TagSerializer,
    ProductSerializer
)


class StockViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows stock to be viewed or edited.
    """
    queryset = Stock.objects.all().order_by('-date_added')
    serializer_class = StockSerializer
    permission_classes = [AllowAny]


class TagViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tag to be viewed or edited.
    """
    queryset = Tag.objects.all().order_by('-id')
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows product to be viewed or edited.
    """
    queryset = Product.objects.all().order_by('-date_created')
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]
