from rest_framework import serializers
from .models import OrderItem, Order, Tracking
from api.inventory.models import Product
from api.accounts.models import Customer
from api.accounts.serializers import CustomerSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    cost = serializers.SerializerMethodField()
    item = serializers.SerializerMethodField()
    price_per_item = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_cost(self, obj):
        """Calculates and returns the cost
           of an order item from the product price.
        """

        product = Product.objects.get(id=obj.product_id)
        return product.price * obj.quantity

    def get_item(self, obj):
        """Returns the cost the product name in an order item.
        """

        return obj.product.name

    def get_price_per_item(self, obj):
        """Returns the price of a single product of an order item.
        """

        return obj.product.price


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True, read_only=True)
    order_id = serializers.CharField(allow_blank=True, required=False)
    grand_total = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data, **kwargs):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data, **kwargs)
        order.order_items.set(items)
        for item in items:
            order_item = OrderItem.objects.get(id=item)
            order_item.is_ordered = True
            order_item.save()
        order.save()
        return order

    def get_grand_total(self, obj):
        """
        Calculates and returns the total cost
        of an order from the order items
        """

        total = 0
        for item in obj.order_items.all():
            item = OrderItemSerializer(OrderItem.objects.get(id=item.id)).data
            total += item['cost']
        return total

    def get_customer_name(self, obj):
        """
        Query and returns the first and last
        name of the customer the order belongs to.
        """

        customer = Customer.objects.get(id=obj.customer_id)
        return f'{customer.first_name} {customer.last_name}'


class TrackingSerializer(serializers.ModelSerializer):
    ship_to = serializers.SerializerMethodField()

    class Meta:
        model = Tracking
        fields = '__all__'

    def get_ship_to(self, obj):
        """
        Query and returns the details of customer the
        order being tracked belongs to.
        """

        customer = Customer.objects.get(username=obj.ship_to)
        return CustomerSerializer(customer).data
