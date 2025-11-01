# Хеш-функція
password = 'password'
hash_password = hash(password)
print('Хеш: ', hash_password)

#Хеш-таблиця
def hash_key(key, m):
    return key % m
m = 15
hash_table = [None for _ in range(m)]
students = [
    (101, "Vladyslav Romanyuk"),
    (102, "Maria Polishchuk"),
    (103, "Denys Shevchenko"),
    (104, "Anastasiia Levchuk"),
    (105, "Ihor Chernenko"),
    (106, "Daryna Petrenko"),
    (107, "Artem Kovalenko"),
    (108, "Sofiia Diachenko"),
    (109, "Nazar Hrytsenko"),
    (110, "Viktoriia Orlova")
]

# Додаємо студента
def add_student(ID, name):
    index = hash_key(ID, m)
    start_index = index
    while hash_table[index] is not None:
        key, existing_name = hash_table[index]
        if key == ID:
            hash_table[index] = (ID, name)
            print(f"Інформацію про студента з ID {ID} оновлено")
            return
        index = (index % m) + 1
        if index == start_index:
            print("Хеш-таблиця переповнена!")
            return
    hash_table[index] = (ID, name)
    print(f"\nДодали студента з ID {ID}")

# Пошук студента
def find_student(ID):
    index = hash_key(ID, m)
    start_index = index
    while hash_table[index] is not None:
        key, name = hash_table[index]
        if key == ID:
            return name
        index = (index % m) + 1
        if index == start_index:
            break
    return None

# Видалення студента
def delete_student(ID):
    index = hash_key(ID, m)
    start_index = index
    while hash_table[index] is not None:
        key, name = hash_table[index]
        if key == ID:
            hash_table[index] = None
            print(f"Студента з ID {ID} видалено.")
            return True
        index = (index % m) + 1
        if index == start_index:
            break
    print(f"Студента з ID {ID} не знайдено.")
    return False

# Вивід таблиці
def display_table():
    print("--Хеш-таблиця студентів--")
    for i, entry in enumerate(hash_table):
        print(f"Індекс {i + 1}: {entry}")

# Наповнення таблиці
for ID, name in students:
    add_student(ID, name)

#Виконання
display_table()

print("Пошук ID 103:", find_student(103))
print("Пошук ID 200:", find_student(200))

print("\nДодаємо нового студента: ")
add_student(103, "Olena Miha")
display_table()
add_student(112, "Maria Kvitkova")
display_table()

print("\nВидаляємо студента 110: ")
delete_student(110)
display_table()
