from simple_sqlite_orm import DBContext
from os import path
from models import User, Product, ProductInBasket


class DB(DBContext):
    def __init__(self) -> None:
        file_dir = path.dirname(path.abspath(__file__))
        file_name = "database.db"
        super().__init__(file_dir, file_name)
        self.users = User(self, 'users')
        self.products = Product(self, 'products')
        self.products_in_basket = ProductInBasket(self, 'products_in_basket')
