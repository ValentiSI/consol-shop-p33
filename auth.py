import re

from db import DB


def is_valid_email(email: str):
    return re.fullmatch(
        r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+",
        email
    )


def is_valid_password(password: str):
    return re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{8,}', password)


def register_user(db: DB):
    email = input("Enter your email address: ")
    password = input("Enter your password: ")
    password_repeat = input("Repeat your password: ")

    if (
        not is_valid_email(email) or
        not is_valid_password(password) or
        password != password_repeat
    ):
        print('Wrong email or password. Try again.')
        return register_user(db)

    return db.users.insert(db.users.model(None, email, password))


def login_user(db: DB):
    email = input("Enter your email address: ")
    password = input("Enter your password: ")

    user = db.users.authenticate(email, password)

    if user is None:
        print("Wrong email or password. Try again.")
        return login_user(db)

    return user


def authorize_user(db: DB):
    print("Please, authorize:")

    choice = input("1. Sign in\n2. Sign up\n")

    if choice == "2":
        return register_user(db)
    elif choice == "1":
        return login_user(db)

    print("Wrong choice. Try again.")
    return authorize_user(db)
