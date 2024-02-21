from db import DB
import pandas as pd

#Отображение продуктов в корзине
def print_product_in_basket(db: DB, user_id: int):
    df = pd.read_sql_query(f'''
                           SELECT products_in_basket.id, products.title, products.price, 
                           products_in_basket.count, (products.price * products_in_basket.count) AS total_price FROM products_in_basket
                           JOIN products ON products_in_basket.product_id = products.id
                           ''', db._connection)
    print(df)
    
db_context = DB()
print_product_in_basket(db_context, int(input('Enter the user ID: ')))

#Удаление продукта из корзины
def delete_product_in_basket(db: DB, product_id: int):
    db.products_in_basket.delete(product_id)
    print(f'Product {product_id} has been removed from the basket')
    
db_context = DB()
delete_product_in_basket(db_context, product_id=int(input('Enter the product id to remove from the basket: ')))
