from rest_framework.serializers import ModelSerializer
from .models import Category, Order


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class OrderSerializer(ModelSerializer):

    class Meta:
        model = Order
        fields = '__all__'
