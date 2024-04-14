import logging
from random import randint

from faker import Faker
from psycopg2 import DatabaseError

from connect import create_connection


fake = Faker(locale='uk-UA')

GROUPS = ("КІТ-122А", "КІТ-123Б", "КІТ-125А")
STUDENTS = 50
TEACHERS = 5
# SUBJECTS = (
#     "Системи штучного інтелекту",
#     "Сучасне програмування, мобільні пристрої та комп’ютерні ігри",
#     "Прикладна комп’ютерна інженерія",
#     "Кібербезпека",
#     "Автоматизація та комп’ютерно-інтегровані технології",
#     "Метрологія та інформаційно-вимірювальна техніка",
# )
SUBJECTS = (
    ("Системи штучного інтелекту", 1),
    ("Сучасне програмування, мобільні пристрої та комп’ютерні ігри", 1),
    ("Прикладна комп’ютерна інженерія", 2),
    ("Кібербезпека", 3),
    ("Автоматизація та комп’ютерно-інтегровані технології", 4),
    ("Метрологія та інформаційно-вимірювальна техніка", 5),
)
GRADES = 5


def insert_groups(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for group_name in GROUPS:
            c.execute(sql_expression, (group_name,))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_students(conn, sql_expression: str):
    c = conn.cursor()    
    try:
        for _ in range(STUDENTS):
            group_id = randint(1, len(GROUPS))
            c.execute(sql_expression, (fake.first_name(), fake.last_name(), group_id))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_teachers(conn, sql_expression: str):
    c = conn.cursor()    
    try:
        for _ in range(TEACHERS):
            c.execute(sql_expression, (fake.first_name(), fake.last_name()))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_subjects(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for tuple_subject in SUBJECTS:
            # teacher_id = randint(1, TEACHERS)
            c.execute(sql_expression, tuple_subject)
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def insert_grades(conn, sql_expression: str):
    c = conn.cursor()
    try:
        for student_id in range(1, STUDENTS + 1):
            for subject_id in range(1, len(SUBJECTS) + 1):
                for _ in range(GRADES):
                    grade = randint(1, 100)
                    grade_date = fake.date_between(start_date='-1y', end_date='today')
                    c.execute(sql_expression, (subject_id, student_id, grade, grade_date))
        conn.commit()
    except DatabaseError as e:
        logging.error(e)
        conn.rollback()
    finally:
        c.close()

def main():
    sql_insert_groups = """
        INSERT INTO groups (group_name) VALUES (%s);
        """
    sql_insert_students = """
        INSERT INTO students (first_name, last_name, group_id) VALUES (%s, %s, %s);
        """
    sql_insert_teachers = """
        INSERT INTO teachers (first_name, last_name) VALUES (%s, %s);
        """
    sql_insert_subjects = """
        INSERT INTO subjects (subject_name, teacher_id) VALUES (%s, %s);
        """
    sql_insert_grades = """
        INSERT INTO grades (subject_id, student_id, grade, grade_date) VALUES (%s, %s, %s, %s);
        """
    
    try:
        with create_connection() as conn:
            if conn is not None:
                # insert_groups(conn, sql_insert_groups)
                # insert_students(conn, sql_insert_students)
                insert_teachers(conn, sql_insert_teachers)
                insert_subjects(conn, sql_insert_subjects)
                # insert_grades(conn, sql_insert_grades)
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)


if __name__ == '__main__':
    main()
