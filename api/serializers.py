""""

from rest_framework.serializers import Serializer, ReadOnlyField, PrimaryKeyRelatedField

from .models import *

class CategoriesSerializer(Serializer):
    class Meta:
        model = Categories
        fields = ['id', 'title']


class OrdersSerializer(Serializer):
    owner = ReadOnlyField(source='owner.username')
    class Meta:
        model = Orders
        fields = ['id', 'date', 'category', 'other_name', 'age', 'description', 'owner']

class UserSerializer(Serializer):
    orders = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']

"""

from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Categories, Orders


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'title']


class OrdersSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Orders
        fields = ['id', 'date', 'category', 'other_name',
                     'age', 'description', 'owner']


class UserSerializer(serializers.ModelSerializer):
    orders = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'orders']
