from db import DB


def main():
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
            '''FOREIGN KEY (product_id) REFERENCES products (id)
            ON UPDATE CASCADE ON DELETE CASCADE'''
        )
    )
    db_context.products_in_basket.insert(
        db_context.products_in_basket.model(
            None,
            3,
            '''FOREIGN KEY (product_id) REFERENCES products (id)
            ON UPDATE CASCADE ON DELETE CASCADE'''
        )
    )
    # # Посмотреть какие таблицы есть в базе данных
    # db_context.execute("SELECT name FROM sqlite_master WHERE type = 'table' AND name != 'sqlite_sequence'")
    # table_names = db_context.getAll()
    # print(', '.join(table[0] for table in table_names))

    # # Посмотреть какие колонки есть в конкретной таблице
    # table_name = input('Введите название таблицы: ')
    # db_context.execute(f"PRAGMA table_info({table_name})")
    # column_info = db_context.getAll()
    # print(', '.join(column[1] for column in column_info))

    # # Посмотреть какие продукты есть в корзине
    # db_context.execute('''
    #     SELECT products_in_basket.id, products.title FROM products_in_basket
    #     JOIN products ON products.id = products_in_basket.product_id
    #     ''')
    # print(*db_context.getAll(), sep='\n')


if __name__ == '__main__':
    main()
