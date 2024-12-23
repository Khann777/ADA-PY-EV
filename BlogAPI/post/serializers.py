from rest_framework import serializers

from .models import Post
from category.models import Category
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(required=True, queryset=Category.objects.all())

    comments = serializers.SerializerMethodField(method_name='get_comments')
    likes = serializers.SerializerMethodField(method_name='get_likes_counter')
    favorites = serializers.SerializerMethodField(method_name='get_favorites_counter') #* Указывать method_name не обязательно

    #? SerializerMethodField() - аналог метода to_representation, но более прост в реализации. Для его работы, нужно написать метод в следующем виде get_<название_метода>.

    def get_comments(self, instance):
        comments = instance.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return serializer.data

    def get_likes_counter(self, instance):
        likes = instance.likes.all().count()
        return likes

    def get_favorites_counter(self, instance):
        favorites = instance.favorites.all().count()
        return favorites

    class Meta:
        model = Post
        fields = '__all__'