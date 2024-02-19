from db import DB


def main():
    db_context = DB()
    print(f'App started with {db_context._connection}')


if __name__ == '__main__':
    main()
