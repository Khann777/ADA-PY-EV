from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

"""
ViewSet не подключаются как обычный класс-представление через метод .as_view()
для подключения viewset понадобится специальный роутер, он импортируется из rest_framework.routers
"""
router = DefaultRouter() #? Создаем объект от класса DefaultRouter
router.register('', ProductViewSet) #? Регистрируем viewset

urlpatterns = [
    path('products/', include(router.urls))
#     path('products-list/', get_products), #* Если вы пишете представление на функциях, вызывать их не нужно
#     path('products-create/', ProductCreateView.as_view()),
#     path('products-detail/<int:pk>', ProductDetailView.as_view()),
#     path('products-list/', ProductListView.as_view()), #* Если вы используете классовое представление, нужно обязательно использовать метод .as_view()
#     path('products-update/<int:pk>/', ProductUpdateView.as_view()),
#     path('product-delete/<int:pk>/', ProductDeleteView.as_view()),
]