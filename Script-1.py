import logging

from psycopg2 import DatabaseError

from connect import create_connection


def select_script(conn, sql_expression: str):
    """ Query SELECT script
    :param conn: Connection object
    :param sql_expression:
    :return:
    """
    c = conn.cursor()
    try:
        c.execute(sql_expression)
        result = c.fetchall()
        for r in result:
            print(r)
    except DatabaseError as e:
        logging.error(e)
    finally:
        c.close()


def main():
    try:
        # читаємо файл зі скриптом
        with open('Script-1.sql', 'r', encoding="utf-8") as f:
            sql = f.read()
        # print(type(sql))

        # створюємо з'єднання з БД
        with create_connection() as conn:
            if conn is not None:
                select_script(conn, sql)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)


if __name__ == '__main__':
    main()



# if __name__ == '__main__':
#     try:
#         with create_connection() as conn:
#             if conn is not None:
#                 c = conn.cursor()
#                 try:
#                     c.execute(sql_expression_01, (13,))
#                     print(c.fetchone())
#                     c.execute(sql_expression_02)
#                     result = c.fetchall()
#                     print(result)
#                     print(result)
#                 except DatabaseError as e:
#                     logging.error(e)
#                 finally:
#                     c.close()
#             else:
#                 print("Error! cannot create the database connection.")
#     except RuntimeError as err:
#         logging.error(err)
