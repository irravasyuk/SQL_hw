from sqlalchemy import create_engine, MetaData, func, and_, or_, extract, insert, update, delete
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

with open('config.json', 'r') as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+pg8000://{db_user}:{db_password}@localhost:5432/academy2'
engine = create_engine(db_url)

# Base = declarative_base()

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

Departments = metadata.tables['departments']
Faculties = metadata.tables['faculties']
Groups = metadata.tables['groups']
Teachers = metadata.tables['teachers']
Lectures = metadata.tables['lectures']
Subjects = metadata.tables['subjects']
Groups_Lectures = metadata.tables['groups_lectures']
Groups_Curators = metadata.tables['groups_curators']
Curators = metadata.tables['curators']


def insert_row(table):
    values = {}

    for column_name in table.columns.keys():
        value = input(f'Введіть значення для стовпчика {column_name}: ')

        if value != '':
            values[column_name] = value

    query = insert(table).values(values)
    session.execute(query)
    session.commit()
    print("Done")


def update_row(table):
    print('Назви стовпчиків:')
    for column_name in table.columns.keys():
        print('\t', column_name)

    condition_column = input('Введіть назву стовпчика для умови: ')
    condition_value = input('Введіть значення для вказаного стовпчика для умови: ')

    values = {}

    for column_name in table.columns.keys():
        value = input(f'Введіть значення для стовпчика {column_name}: ')

        if value != '':
            values[column_name] = value

    column = getattr(table.c, condition_column)

    query = update(table) \
        .where(column == column.type.python_type(condition_value)) \
        .values(values)

    session.execute(query)
    session.commit()
    print("Done")


def delete_row(table):
    print('Назви стовпчиків:')
    for column_name in table.columns.keys():
        print('\t', column_name)

    condition = input('Введіть умову для одного стовпчика: ')

    query = delete(table).where(eval('table.c.' + condition))

    session.execute(query)
    session.commit()
    print("Done")


def report_all_groups():
    result = session.query(Groups).all()
    if result:
        for row in result:
            group_info = ' '.join(map(str, row))
            print(group_info)


def report_all_teachers():
    result = session.query(Teachers).all()
    if result:
        for row in result:
            teacher_info = ' '.join(map(str, row))
            print(teacher_info)


def report_all_departments():
    result = session.query(Departments.c.name).all()

    if result:
        for row in result:
            print(f"{row.name}")


def report_teachers_in_group(group_name):
    result = session.query(Teachers.c.name, Teachers.c.surname) \
        .join(Groups_Lectures, Teachers.c.id == Groups_Lectures.c.id) \
        .join(Groups, Groups_Lectures.c.group_id == Groups.c.id) \
        .filter(Groups.c.name == group_name).all()
    for row in result:
        print(f"{row.name} {row.surname}")


def report_departments_and_groups():
    result = session.query(Departments.c.name.label("department_name"), Groups.c.name.label("group_name")) \
        .join(Groups, Groups.c.department_id == Departments.c.id).all()
    if result:
        for row in result:
            print(f"{row.department_name} {row.group_name}")


def report_department_with_max_groups():
    result = session.query(Departments.c.name) \
        .join(Groups, Departments.c.id == Groups.c.department_id) \
        .group_by(Departments.c.name) \
        .order_by(func.count(Groups.c.id).desc()).first()
    print(result.name)


def report_department_with_min_groups():
    result = session.query(Departments.c.name) \
        .join(Groups, Departments.c.id == Groups.c.department_id) \
        .group_by(Departments.c.name) \
        .order_by(func.count(Groups.c.id).asc()).first()
    print(result.name)


def report_subjects_by_teacher(teacher_name):
    result = session.query(Subjects.c.name) \
        .join(Lectures, Subjects.c.id == Lectures.c.subject_id) \
        .join(Teachers, Lectures.c.id == Teachers.c.id) \
        .filter(Teachers.c.name == teacher_name).all()
    for row in result:
        print(row.name)


def report_departments_by_subject(subject_name):
    result = session.query(Departments.c.name) \
        .join(Groups, Groups.c.id == Departments.c.id) \
        .join(Groups_Lectures, Groups.c.id == Groups_Lectures.c.group_id) \
        .join(Lectures, Groups_Lectures.c.lecture_id == Lectures.c.id) \
        .join(Subjects, Lectures.c.subject_id == Subjects.c.id) \
        .filter(Subjects.c.name == subject_name).all()
    for row in result:
        print(f"{row.name}")


def report_groups_by_faculty(faculty_name):
    result = session.query(Groups.c.name) \
        .join(Departments, Groups.c.department_id == Departments.c.id) \
        .join(Faculties, Departments.c.id == Faculties.c.id) \
        .filter(Faculties.c.name == faculty_name).all()
    for row in result:
        print(row.name)


def report_subjects_and_teachers_with_max_lectures():
    result = session.query(Subjects.c.name.label('subject_name'), Teachers.c.name.label('teacher_name'),
                           Teachers.c.surname.label('teacher_surname')) \
        .join(Lectures, Subjects.c.id == Lectures.c.subject_id) \
        .join(Teachers, Lectures.c.id == Teachers.c.id) \
        .group_by(Subjects.c.name, Teachers.c.name, Teachers.c.surname) \
        .order_by(func.count(Lectures.c.id).desc()).all()
    for row in result:
        print(f"{row.subject_name} - {row.teacher_name} {row.teacher_surname}")


def report_subject_with_min_lectures():
    result = session.query(Subjects.c.name) \
        .join(Lectures, Subjects.c.id == Lectures.c.subject_id) \
        .group_by(Subjects.c.name) \
        .order_by(func.count(Lectures.c.id).asc()).first()
    print(result.name)


def report_subject_with_max_lectures():
    result = session.query(Subjects.c.name) \
        .join(Lectures, Subjects.c.id == Lectures.c.subject_id) \
        .group_by(Subjects.c.name) \
        .order_by(func.count(Lectures.c.id).desc()).first()
    print(result.name)


def main_menu():
    while True:
        print("1. Вставити рядок в таблицю")
        print("2. Оновити рядок в таблиці")
        print("3. Видалити рядок з таблиці")
        print("4. Звіти")
        print("0. Вийти")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            table_name = input("Введіть назву таблиці, в яку вставляємо рядок: ")
            table = metadata.tables[table_name]
            insert_row(table)
        elif choice == "2":
            table_name = input("Введіть назву таблиці, в якій оновлюємо рядок: ")
            table = metadata.tables[table_name]
            update_row(table)
        elif choice == "3":
            table_name = input("Введіть назву таблиці, з якої видаляємо рядок(-и): ")
            table = metadata.tables[table_name]
            delete_row(table)

        elif choice == "4":
            print("1. Вивести інформацію про всі навчальні групи")
            print("2. Вивести інформацію про всіх викладачів")
            print("3. Вивести назви усіх кафедр")
            print("4. Вивести викладачів, які ведуть лекції для заданої групи")
            print("5. Вивести назви кафедр та груп")
            print("6. Вивести назву кафедри з найбільшою кількістю груп")
            print("7. Вивести назву кафедри з найменшою кількістю груп")
            print("8. Вивести предмети, які викладає певний викладач")
            print("9. Вивести кафедри, що проводять заняття з певного предмету")
            print("10. Вивести групи, що належать до факультету")
            print("11. Вивести предмети та викладачів, які проводять найбільшу кількість лекцій")
            print("12. Вивести предмет з найменшою кількістю лекцій")
            print("13. Вивести предмет з найбільшою кількістю лекцій")

            report_choice = input("Оберіть опцію для звіту: ")

            if report_choice == "1":
                report_all_groups()
            elif report_choice == "2":
                report_all_teachers()
            elif report_choice == "3":
                report_all_departments()
            elif report_choice == "4":
                group_name = input("Введіть назву групи: ")
                report_teachers_in_group(group_name)
            elif report_choice == "5":
                report_departments_and_groups()
            elif report_choice == "6":
                report_department_with_max_groups()
            elif report_choice == "7":
                report_department_with_min_groups()
            elif report_choice == "8":
                teacher_name = input("Введіть ім'я викладача: ")
                report_subjects_by_teacher(teacher_name)
            elif report_choice == "9":
                subject_name = input("Введіть назву предмета: ")
                report_departments_by_subject(subject_name)
            elif report_choice == "10":
                faculty_name = input("Введіть назву факультету: ")
                report_groups_by_faculty(faculty_name)
            elif report_choice == "11":
                report_subjects_and_teachers_with_max_lectures()
            elif report_choice == "12":
                report_subject_with_min_lectures()
            elif report_choice == "13":
                report_subject_with_max_lectures()
            else:
                print("Невірний вибір. Будь ласка, оберіть знову.")

        elif choice == "0":
            break

        else:
            print("Невірний вибір. Будь ласка, оберіть знову.")


if __name__ == "__main__":
    main_menu()

session.close()
