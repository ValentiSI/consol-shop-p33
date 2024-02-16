from simple_sqlite_orm import column_types, Table


class User(Table):
    id = column_types.IdColumn()
    email = column_types.TextColumn(unique=True)
    password = column_types.TextColumn()


class Product(Table):
    id = column_types.IdColumn()
<<<<<<< HEAD
    title = column_types.TextColumn(unique=True)
=======
    title = column_types.TextColumn(unique=True)
>>>>>>> 75f846791361390cfca2fc0579e8fd6ef0a1b739
    price = column_types.NumericColumn()


class ProductInBasket(Table):
    id = column_types.IdColumn()
    product_id = column_types.IntegerColumn()