from db import DB
from functools import reduce


def display_products(db_context: DB):
    products = list(db_context.products.getAll())
    if len(products) == 0:
        print("No products")
        return
    names = [column.name for column in db_context.products.columns]
    id_len = max(len(names[0]), len(str(products[-1].id)))
    price_len = reduce(
        lambda x, y: max(x, len(f"{y.price:.2f}")), products, len(names[2])
    )

    print(f"{names[0]: >{id_len}} | {names[1]: ^20} | {names[2] : ^{price_len}}")

    for product in products:
        print(
            f"{product.id: >{id_len}} | {product.title: ^20} | {product.price : ^{price_len}.2f}$"
        )

def select_product(db_context: DB, prod_id: int):
    prod_id =int(input('Enter product id: '))
    product = db_context.products.get(prod_id)
    if not product:
        print("No such product")
        return
    print(f"{product.title} | {product.price:.2f}$")
    
    

# pandas variant
# def display_products(db_context: DB):
#     products = list(db_context.products.getAll())
#     if not products:
#         print("No products")
#         return
#     df = pd.DataFrame([(p.id, p.title, f'{p.price:.2f}$') for p in products], columns=['id', 'title', 'price'])

#     print(df.to_string(index=False))
