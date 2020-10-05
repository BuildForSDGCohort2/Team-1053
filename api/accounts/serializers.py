from allauth.account.adapter import get_adapter
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token

from .models import Customer, User


class UserRegisterSerializer(RegisterSerializer):
    """serializer for UserRegisterSerializer."""

    class Meta:
        model = User
        fields = '__all__'

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'password1': self.validated_data.get('password1', ''),
            'password2': self.validated_data.get('password2', ''),
            'email': self.validated_data.get('email', '')

        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        user.save()
        adapter.save_user(request, user, self)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'last_login',
            'date_joined',
        )


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Customer
        fields = '__all__'

    def create(self, validated_data, **kwargs):
        user = self.context['request'].user
        customer = Customer(
            **validated_data, **kwargs,
            user=user
        )
        customer.save()
        return customer


class TokenSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Token
        fields = ('key', 'user')

    def get_user(self, obj):
        user_data = UserSerializer(obj.user).data
        return {
            'id': user_data.get('id'),
            'username': user_data.get('username'),
            'email': user_data.get('email'),
            'first_name': user_data.get('first_name'),
            'last_name': user_data.get('last_name'),
            'is_staff': user_data.get('is_staff'),
            'last_login': user_data.get('last_login')
        }
