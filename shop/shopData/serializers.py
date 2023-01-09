from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Category, Order


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = ('name',)


class OrderSerializer(ModelSerializer):
    category = PrimaryKeyRelatedField(queryset=Category.objects.all())

    class Meta:
        model = Order
        fields = '__all__'
