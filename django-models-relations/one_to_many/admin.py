from django.contrib import admin
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title'] #* это то, что будет отображаться при листинге объектов
    list_filter = ['price'] #* поля, по которым можно будет проходить фильтром
    search_fields = ['title'] #* поле, по которому мы можем провести поиск по нашим объектам

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
