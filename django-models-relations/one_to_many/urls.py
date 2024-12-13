from django.urls import path
from .views import get_products, ProductListView, ProductDeleteView

urlpatterns = [
    path('products-list/', get_products), #* Если вы пишете представление на функциях, вызывать их не нужно
    path('products-cbv/', ProductListView.as_view()), #* Если вы используете классовое представление, нужно обязательно использовать метод .as_view()
    path('products-cbv/', ProductListView.as_view()),
    path('product-delete/<int:pk>/', ProductDeleteView.as_view()),
]