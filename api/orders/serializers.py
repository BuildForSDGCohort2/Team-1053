from rest_framework import serializers
from .models import OrderItem, Order, Tracking
from api.inventory.models import Product


class OrderItemSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()
    item = serializers.SerializerMethodField()
    price_per_item = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_cost(self, obj):
        print(obj.__dict__)
        product = Product.objects.get(id=obj.product_id)
        return product.price * obj.quantity

    def get_item(self, obj):
        return obj.product.name

    def get_price_per_item(self, obj):
        return obj.product.price


class OrderSerializer(serializers.ModelSerializer):
    order_id = serializers.CharField(allow_blank=True, required=False)
    total_cost = serializers.SerializerMethodField()
    items = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def get_total_cost(self, obj):
        total = 0
        for item in obj.items.all():
            item = OrderItemSerializer(OrderItem.objects.get(id=item.id)).data
            total += item['cost']
        return total

    def get_items(self, obj):
        items = []
        for item in obj.items.all():
            items.append(
                OrderItemSerializer(
                    OrderItem.objects.get(id=item.id)
                ).data
            )
        return items


class TrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tracking
        fields = '__all__'
