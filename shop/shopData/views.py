from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
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


class OrderRetrieveUpdateAPIView(APIView):
    serializer_class = OrderSerializer
    permission_classes = (AllowAny,)

    def get(self, request, id):
        serializer = self.serializer_class(Order.objects.filter(category=Category.objects.get(pk=id)), many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
