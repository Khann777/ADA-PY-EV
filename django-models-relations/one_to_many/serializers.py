from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__' #* ['id', 'title', 'price']
        #*
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return value

        #? Есть 2 метода для валидации в сериализаторах, validate и validate_<field>, validate(self, attrs) - attrs - словарь с данными из запроса, сам метод проверяет все данные. validate_<field>(self, <fields>) - валидирует какое-то определенное поле, если валидация прошла, то нужно обязательно вернуть это поле
