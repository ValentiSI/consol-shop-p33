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
    print('App started')


if __name__ == '__main__':
    main()
