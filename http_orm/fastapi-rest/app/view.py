from typing import List

from fastapi import APIRouter, HTTPException

from db_settings import SessionLocal

from .serializers import *
from .models import Product

db = SessionLocal()
router = APIRouter()

# Листинг товара (get запрос)
@router.get('/products/list', response_model=List[ProductListSerializer], status_code=200)
def products_list():
    products = db.query(Product).all()
    return products


# retrieve(detail) - запрос на получение всей информации о продукте (детальный обзор)
@router.get('/products/detail/{id}', response_model=ProductDetailSerializer, status_code=200)
def product_detail(id: int):
    product = db.query(Product).get(id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    return product

@router.post('/products/create', status_code=201)
def product_create(data: ProductSerializer):
    new_product = Product(
        title=data.title,
        price=data.price,
        quantity=data.quantity,
        description=data.description,
    )
    db.add(new_product)
    db.commit()
    return {
        'msg': 'Product created',
    }

@router.patch('/products/update/{id}', status_code=200)
def product_update(id: int, data: ProductSerializer):
    product = db.query(Product).get(id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    if data.title:
        product.title = data.title
    if data.price:
        product.price = data.price
    if data.quantity:
        product.quantity = data.quantity
    if data.description:
        product.description = data.description
    db.commit()
    return {
        'msg': 'Product updated',
    }

@router.delete('/products/delete/{id}', status_code=204)
def product_delete(id: int):
    product = db.query(Product).get(id)
    if not product:
        raise HTTPException(status_code=404, detail='Product not found')
    db.delete(product)
    db.commit()