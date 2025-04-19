import psycopg2
import csv
from tabulate import tabulate

# Дерекқормен қосылу
conn = psycopg2.connect(host="localhost", dbname="pp2", user="postgres",
                        password="postgres")
cur = conn.cursor()

# Кесте жасау
cur.execute("""
CREATE TABLE IF NOT EXISTS phonebook (
    user_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    surname VARCHAR(255) NOT NULL, 
    phone VARCHAR(255) NOT NULL
)
""")

# Мәлімет енгізу
def insert_data():
    print('CSV файлын жүктеу үшін "csv", консольдан енгізу үшін "con" деп жазыңыз:')
    method = input().lower()
    if method == "con":
        name = input("Аты: ")
        surname = input("Тегі: ")
        phone = input("Телефон: ")
        cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", (name, surname, phone))
    elif method == "csv":
        filepath = input("Файл жолын енгізіңіз (.csv): ")
        with open(filepath, 'r') as f:
            reader = csv.reader(f)
            next(reader)  # Тақырып жолын өткізіп жібереміз
            for row in reader:
                if len(row) != 3:
                    print(f"Қате жол өткізіледі: {row}")
                    continue
                cur.execute("INSERT INTO phonebook (name, surname, phone) VALUES (%s, %s, %s)", tuple(row))
    conn.commit()

# Мәлімет жаңарту
def update_data():
    valid_columns = ['name', 'surname', 'phone']
    column = input('Қай бағанды өзгерткіңіз келеді (name, surname, phone): ')
    if column not in valid_columns:
        print("Қате баған атауы!")
        return
    value = input(f"Қазіргі {column}: ")
    new_value = input(f"Жаңа {column}: ")
    cur.execute(f"UPDATE phonebook SET {column} = %s WHERE {column} = %s", (new_value, value))
    conn.commit()

# Мәлімет жою
def delete_data():
    phone = input('Жойғыңыз келетін телефон нөмірін енгізіңіз: ')
    cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
    conn.commit()

# Мәлімет іздеу
def query_data():
    valid_columns = ['name', 'surname', 'phone']
    column = input("Қай баған арқылы іздегіңіз келеді (name, surname, phone): ")
    if column not in valid_columns:
        print("Қате баған атауы!")
        return
    value = input(f"{column} мәнін енгізіңіз: ")
    cur.execute(f"SELECT * FROM phonebook WHERE {column} = %s", (value,))
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Аты", "Тегі", "Телефон"]))

# Барлық мәліметтерді көрсету
def display_data():
    cur.execute("SELECT * FROM phonebook;")
    rows = cur.fetchall()
    print(tabulate(rows, headers=["ID", "Аты", "Тегі", "Телефон"], tablefmt='fancy_grid'))

# Негізгі цикл
while True:
    print("""
    Командалар тізімі:
    1. "i" — МӘЛІМЕТ ҚОСУ
    2. "u" — МӘЛІМЕТ ЖАҢАРТУ
    3. "q" — МӘЛІМЕТ ІЗДЕУ
    4. "d" — МӘЛІМЕТ ЖОЮ
    5. "s" — БАРЛЫҚ МӘЛІМЕТТІ КӨРУ
    6. "f" — БАҒДАРЛАМАНЫ ЖАБУ
    """)
    command = input("Команда енгізіңіз: ").lower()

    if command == "i":
        insert_data()
    elif command == "u":
        update_data()
    elif command == "d":
        delete_data()
    elif command == "q":
        query_data()
    elif command == "s":
        display_data()
    elif command == "f":
        print("Бағдарлама жабылды. Сау болыңыз!")
        break

# Қосылымды жабу
conn.commit()
cur.close()
conn.close()
