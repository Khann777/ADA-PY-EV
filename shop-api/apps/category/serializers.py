from rest_framework import serializers
from .models import Category

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_children(self, instance):
        children = instance.children.all()
        return CategorySerializer(children, many=True).data if children else None