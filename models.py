from simple_sqlite_orm import Table, column_types


class User(Table):
    id = column_types.IdColumn()
    email = column_types.TextColumn(unique=True)
    password = column_types.TextColumn()


class Product(Table):
    id = column_types.IdColumn()
    title = column_types.TextColumn(unique=True)
    price = column_types.NumericColumn()
