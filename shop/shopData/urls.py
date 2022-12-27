from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'order', OrderViewSet, basename='order')

urlpatterns = router.urls
