from db import DB
from models import ProductInBasket


def add_product_in_basket(db, user_id, product_id):
    products = list(db.products_in_basket.getAll(
        filter=f'product_id = {product_id} AND user_id = {user_id}'
    ))

    if len(products) == 0:
        db.products_in_basket.insert(
            db.products_in_basket.model(
                None,
                product_id,
                user_id,
                input('Введите количество: ')
            )
        )
    else:
        existing_product = products[0]
        existing_product.count += int(input('Введите количество: '))
        db.products_in_basket.update(existing_product)

    print('Товар добавлен в корзину')



