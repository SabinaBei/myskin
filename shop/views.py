# from django.shortcuts import render, get_object_or_404
# from cart.forms import CartAddProductForm
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from shop.models import Category, Product
from shop.serializers import ProductSerializers
from rest_framework import viewsets
from django_filters import rest_framework as filters


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['price']


class ProductViewSet(viewsets.ModelViewSet):
    '''предоставляет для фронта информацию о курсах'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['product']
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']
    filterset_class = ProductFilter



# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request, 'shop/product/list.html',
#               {'category': category,
#                'categories': categories,
#                'products': products})
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request, 'shop/product/detail.html', {'product': product})
#
# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     cart_product_form = CartAddProductForm()
#     return render(request, 'shop/product/detail.html',
#                 {'product': product,
#                 'cart_product_form': cart_product_form})
