from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, OrderViewSet, OrderRetrieveUpdateAPIView

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = [
    path('ordersbycat/<int:id>/', OrderRetrieveUpdateAPIView.as_view())
]
urlpatterns += router.urls
