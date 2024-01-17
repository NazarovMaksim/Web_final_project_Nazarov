import sqlite3
import data
# Создание подключения к базе данных
conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
cursor = conn.cursor()


# Создаем таблицу Товары
cursor.execute('''
    CREATE TABLE Goods (
        id_goods INTEGER PRIMARY KEY,
        name VARCHAR(90)
    )
''')

# Создаем таблицу Модели
cursor.execute('''
    CREATE TABLE Models (
        code_model INTEGER PRIMARY KEY,
        name VARCHAR(90),
        id_goods INTEGER,
        model_price REAL,
        FOREIGN KEY (id_goods) REFERENCES Goods(id_goods)
    )
''')

# Создаем таблицу Поступления
cursor.execute('''
    CREATE TABLE Incomes (
        id_income INTEGER PRIMARY KEY,
        code_model INTEGER,
        income_date DATE,
        count INTEGER,
        id_worker INTEGER,
        id_room INTEGER,
        FOREIGN KEY (code_model) REFERENCES Models(code_model),
        FOREIGN KEY (id_worker) REFERENCES Workers(id_worker),
        FOREIGN KEY (id_room) REFERENCES Rooms(id_room)
    )
''')

# Создаем таблицу Кладовщики
cursor.execute('''
    CREATE TABLE Workers (
        id_worker INTEGER PRIMARY KEY,
        full_name VARCHAR(90),
        phone_num VARCHAR(11)
    )
''')

# Создаем таблицу Складские_помещения
cursor.execute('''
    CREATE TABLE Rooms (
        id_room INTEGER PRIMARY KEY,
        type_room VARCHAR(90)
    )
''')

# Удаление существующих данных из таблиц перед вставкой
cursor.execute('DELETE FROM Goods')
cursor.execute('DELETE FROM Models')
cursor.execute('DELETE FROM Incomes')
cursor.execute('DELETE FROM Workers')
cursor.execute('DELETE FROM Rooms')

# Вставка данных в таблицу Goods
cursor.executemany('INSERT INTO Goods (id_goods, name) VALUES (?, ?)', data.Goods_data)

# Вставка данных в таблицу Models
cursor.executemany('INSERT INTO Models (code_model, name, id_goods, model_price) VALUES (?, ?, ?, ?)', data.Models_data)

# Вставка данных в таблицу Incomes
cursor.executemany('INSERT INTO Incomes (id_income, code_model, income_date, count,id_worker,id_room) VALUES (?, ?, ?, ?, ?, ?)', data.Incomes_data)

# Вставка данных в таблицу Workers
cursor.executemany('INSERT INTO Workers (id_worker, full_name, phone_num) VALUES (?, ?, ?)', data.Workers_data)

# Вставка данных в таблицу Rooms
cursor.executemany('INSERT INTO Rooms (id_room, type_room) VALUES (?, ?)', data.Rooms_data)

# Сохранение изменений и закрытие соединения
conn.commit()
conn.close()