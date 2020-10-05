from api.accounts.models import Customer
from api.accounts.serializers import CustomerSerializer
from api.inventory.models import Product
from api.utils.helpers import generate_id
from rest_framework import serializers

from .models import Order, OrderItem, Tracking


class OrderItemSerializer(serializers.ModelSerializer):
    product_detail = serializers.SerializerMethodField()

    class Meta:
        model = OrderItem
        fields = '__all__'

    def get_product_detail(self, obj):
        product = Product.objects.get(pk=obj.product_id)
        return {
            'name': product.name,
            'price': product.price
        }


class OrderSerializer(serializers.ModelSerializer):
    orderitem_set = OrderItemSerializer(
        many=True, required=False, read_only=True
    )
    order_id = serializers.CharField(allow_blank=True, required=False)
    grand_total = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data, **kwargs):
        user = self.context['request'].user
        customer = Customer.objects.get(user=user)
        items = self.context['request'].data.get('items')
        order = Order(
            customer=customer,
            order_id=generate_id(),
            **validated_data, **kwargs
        )
        order.save()
        for item in items:
            id = item.pop('product')
            instance = Product.objects.get(id=id)
            order_item = OrderItem(order=order, **item, product=instance)
            order_item.save()
        return order

    def get_grand_total(self, order):
        """
        Calculates and returns the total cost
        of an order from the order items
        """

        total = 0
        items = order.orderitem_set.all()
        print(items)
        for item in items:
            total += item.cost
        return total

    def get_customer_name(self, obj):
        """
        Query and returns the first and last
        name of the customer the order belongs to.
        """

        customer = Customer.objects.get(id=obj.customer_id)
        return f'{customer.user.first_name} {customer.user.last_name}'


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
