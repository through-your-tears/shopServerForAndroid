from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Category, Order
from .serializers import CategorySerializer, OrderSerializer

# Create your views here.


class CategoryViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class OrderViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
