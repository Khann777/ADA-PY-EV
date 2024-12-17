from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer, ProductListSerializer

#* FBV (Function Based Views) - представления, которые написаны на функциях
#* CBV (Class Based Views) - представления, которые написаны на классах

# def get_products(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         data = []
#         for product in products:
#             data.append({
#                 'id': product.id,
#                 'title': product.title,
#                 'price': product.price,
#                 'description': product.description,
#                 'quantity': product.quantity,
#                 'category': product.category.name,
#             })
#         return JsonResponse(data, safe=False)

#? APIView - класс, который позволяет нам писать представление на классах
# class ProductListView(APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#         return Response(serializer.data)
#
# class ProductCreateView(APIView):
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class ProductDeleteView(APIView):
#     def delete(self, request, pk):
#         product = Product.objects.filter(pk=pk).first()
#         if not product:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         product.delete()
#         return Response({'message': 'Product deleted'}, status=status.HTTP_204_NO_CONTENT)
#
#
# class ProductPartialUpdateView(APIView):
#     def patch(self, request, pk):
#         try:
#             product = Product.objects.get(pk=pk)
#         except Product.DoesNotExist:
#             return Response({'message': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
#         serializer = ProductSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
generics - те же классовые представления, но в них уже заранее написана вся логика для CRUD операций
"""

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer()

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer()

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()

class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer()

class ProductDeleteView(generics.DestroyAPIView):
    queryset = Product.objects.all()



class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductSerializer