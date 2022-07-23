from django.urls import path
from shop.views import ProductViewSet

urlpatterns = [
    path('', ProductViewSet.as_view({'get': 'list', 'post': 'create', 'delete': 'destroy'}), name='product'),
    path('<int:pk>/', ProductViewSet.as_view({'get' : 'retrieve', 'put' : 'update', 'patch': 'update', 'delete' : 'destroy'}), name='product'),
]
