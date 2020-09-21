from rest_framework import serializers
from allauth.account.adapter import get_adapter
from rest_framework.authtoken.models import Token
from rest_auth.registration.serializers import RegisterSerializer
from .models import User, Customer


class UserRegisterSerializer(RegisterSerializer):
    """serializer for UserRegisterSerializer."""

    class Meta:
        model = User
        fields = '__all__'

    def get_cleaned_data(self):
        return {
            'username': self.validated_data.get('username', ''),
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
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


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
            'first_name': user_data.get('first_name'),
            'last_name': user_data.get('last_name'),
            'is_staff': user_data.get('is_staff'),
            'last_login': user_data.get('last_login')
        }
