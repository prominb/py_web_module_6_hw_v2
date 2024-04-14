import logging
from psycopg2 import DatabaseError

from connect import create_connection


def create_table(conn, sql_expression: str):
    """ create a table from the create_table_sql statement
    :param sql_expression:
    :param conn: Connection object
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()


def main():
    # sql_create_users_table = """
    # CREATE TABLE IF NOT EXISTS users (
    #  id SERIAL PRIMARY KEY,
    #  name VARCHAR(120),
    #  email VARCHAR(120),
    #  password VARCHAR(120),
    #  age SMALLINT CHECK(age > 18 AND age < 75)
    # );
    # """

    try:
        # читаємо файл зі скриптом для створення БД
        with open('create-tables.sql', 'r', encoding="utf-8") as f:
            sql = f.read()
        # print(type(sql))

        # створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
        with create_connection() as conn:
            if conn is not None:
                # create_table(conn, sql_create_users_table)
                create_table(conn, sql)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)


if __name__ == '__main__':
    main()
