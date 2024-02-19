from db import DB

with open('database.db', 'w+'):
    pass

db_context = DB()

db_context.users.insert(
    db_context.users.model(
        None,
        'Ali@gmail.com',
        '123456'
    )
)
db_context.products.insert(
    db_context.products.model(
        None,
        'Телевизор',
        51999
    )
)
db_context.products.insert(
    db_context.products.model(
        None,
        'Чайник',
        5999
    )
)
db_context.products.insert(
    db_context.products.model(
        None,
        'Ноутбук',
        32999
    )
)
db_context.products_in_basket.insert(
    db_context.products_in_basket.model(
        None,
        1,
        1,
        1
    )
)
db_context.products_in_basket.insert(
    db_context.products_in_basket.model(
        None,
        3,
        1,
        2
    )
)


print(*db_context.products_in_basket.getAll())
print(*db_context.products.getAll())
print(*db_context.users.getAll())
