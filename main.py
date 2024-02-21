from db import DB
from auth import authorize_user

def main():
    db_context = DB()
    user = authorize_user(db_context)
    print(f'App started with {db_context._connection}')


if __name__ == '__main__':
    main()
