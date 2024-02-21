from models import User, ProductInBasket

def delete_user(user_id):
    
    user = User.get(id=user_id)

    if user:
        ProductInBasket.delete().where(ProductInBasket.user_id == user_id).execute()

        user.delete_instance()
        print(f"Пользователь с id {user_id} успешно удален.")
    else:
        print(f"Пользователь с id {user_id} не найден.")