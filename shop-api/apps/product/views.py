from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination


from apps.product.models import Product, ProductImage
from apps.product.serializers import ProductDetailSerializer, ProductListSerializer, ProductCreateSerializer, \
    ProductImageSerializer
from apps.generals.permissions import IsProductOwner, IsOwner


class StandardResultPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page'

class ProductList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticated, ]
    pagination_class = StandardResultPagination

class ProductDetail(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer
    permission_classes = [permissions.IsAuthenticated, ]

class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAuthenticated, ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductImageAddView(generics.CreateAPIView):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    # permission_classes = [IsProductOwner, ]