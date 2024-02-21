from simple_sqlite_orm import column_types, Table


class User(Table):
    id = column_types.IdColumn()
    email = column_types.TextColumn(unique=True)
    password = column_types.TextColumn()

    def authenticate(self, email, password):
        user = self.getBy(self.email, email)

        if user.password != password:
            return None

        return user


class Product(Table):
    id = column_types.IdColumn()
    title = column_types.TextColumn(unique=True)
    price = column_types.NumericColumn()


class ProductInBasket(Table):
    id = column_types.IdColumn()
    product_id = column_types.IntegerColumn()
    user_id = column_types.IntegerColumn()
    count = column_types.IntegerColumn()
