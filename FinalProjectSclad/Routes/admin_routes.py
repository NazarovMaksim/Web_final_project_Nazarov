import datetime
import re

from fastapi.responses import JSONResponse
from Authorization.authorization import KeycloakJWTBearerHandler, HTTPException
import sqlite3
from fastapi import APIRouter, Depends
import json
from Models.models import Goods_model, Models_model,Incomes_model,Workers_model, Rooms_model
admin_router = APIRouter(
    tags=["Administrator"]
)

@admin_router.get("/Goods")
def get_Goods(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Goods;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@admin_router.get("/Models")
def get_Models(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Models;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@admin_router.get("/Incomes")
def get_Incomes(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Incomes;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@admin_router.get("/Workers")
def get_Workers(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Workers;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@admin_router.get("/Rooms")
def get_Rooms(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Rooms;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@admin_router.post("/Goods")
def post_Goods(Goods_info:Goods_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT id_goods FROM Goods WHERE
        id_goods = {Goods_info.id_goods};
    ''')
    data = cursor.fetchall()
    print(data)
    if len(data)!=0:
        return JSONResponse(status_code=404, content={"message": "Товар с таким кодом уже существует"})
    if Goods_info.name == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})
    cursor.execute(f'INSERT INTO Goods (id_goods, name) VALUES ({Goods_info.id_goods},"{Goods_info.name}")')
    conn.commit()
    conn.close()
    return("Товар усепшно добавлен")

@admin_router.put("/Goods")
def put_Goods(Goods_info:Goods_model, role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT id_goods FROM Goods WHERE id_goods = {Goods_info.id_goods};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Товар с таким кодом не найден"})

    if Goods_info.name == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})

    # Обновление данных о работнике
    cursor.execute(f'''
        UPDATE Goods
        SET name = "{Goods_info.name}"
        WHERE id_goods = {Goods_info.id_goods};
    ''')
    conn.commit()
    conn.close()
    return {"message": f"Данные товара с кодом {Goods_info.id_goods} успешно обновлены"}

@admin_router.delete("/Goods")
def delete_Goods(Goods_info:Goods_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT id_goods FROM Goods WHERE id_goods = {Goods_info.id_goods};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Товар с таким кодом не найден"})

    # Удаление данных о работнике
    cursor.execute(f'DELETE FROM Goods WHERE id_goods = {Goods_info.id_goods};')
    conn.commit()
    conn.close()
    return {"message": f"Данные о товаре с кодом {Goods_info.id_goods} успешно удалены"}

@admin_router.post("/Rooms")
def post_Rooms(Rooms_info:Rooms_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT id_room FROM Rooms WHERE
        id_room = {Rooms_info.id_room};
    ''')
    data = cursor.fetchall()
    print(data)
    if len(data)!=0:
        return JSONResponse(status_code=404, content={"message": "Помещение с таким кодом уже существует"})
    if Rooms_info.type_room == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})
    if (Rooms_info.type_room != "малое") & (Rooms_info.type_room != "среднее") & (Rooms_info.type_room != "большое"):
        return JSONResponse(status_code=404, content={"message": "Помещение должно быть либо малое, либо среднее, либо большое"})

    cursor.execute(f'INSERT INTO Rooms (id_room, type_room) VALUES ({Rooms_info.id_room},"{Rooms_info.type_room}")')
    conn.commit()
    conn.close()
    return("Помещение усепшно добавлено")

@admin_router.put("/Rooms")
def put_Rooms(Rooms_info:Rooms_model, role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT id_room FROM Rooms WHERE id_room = {Rooms_info.id_room};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Помещение с таким кодом не найдено"})

    if Rooms_info.type_room == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})
    if (Rooms_info.type_room != "малое") & (Rooms_info.type_room != "среднее") & (Rooms_info.type_room != "большое"):
        return JSONResponse(status_code=404, content={"message": "Помещение должно быть либо малое, либо среднее, либо большое"})
    # Обновление данных о работнике
    cursor.execute(f'''
        UPDATE Rooms
        SET type_room = "{Rooms_info.type_room}"
        WHERE id_room = {Rooms_info.id_room};
    ''')
    conn.commit()
    conn.close()
    return {"message": f"Данные помешения с кодом {Rooms_info.id_room} успешно обновлены"}

@admin_router.delete("/Rooms")
def delete_Rooms(Rooms_info:Rooms_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT id_room FROM Rooms WHERE id_room = {Rooms_info.id_room};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Помещение с таким кодом не найдено"})

    # Удаление данных о работнике
    cursor.execute(f'DELETE FROM Rooms WHERE id_room = {Rooms_info.id_room};')
    conn.commit()
    conn.close()
    return {"message": f"Данные о помещении с кодом {Rooms_info.id_room} успешно удалены"}

@admin_router.post("/Models")
def post_Models(Models_info:Models_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT code_model FROM Models WHERE
        code_model = {Models_info.code_model};
    ''')
    data = cursor.fetchall()
    print(data)
    if len(data)!=0:
        return JSONResponse(status_code=404, content={"message": "Модель с таким кодом уже существует"})
    if Models_info.name == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})
    cursor.execute(f'INSERT INTO Models (code_model, name, id_goods, model_price) VALUES ({Models_info.code_model},"{Models_info.name}",{Models_info.id_goods},{Models_info.model_price})')
    conn.commit()
    conn.close()
    return("Модель усепшно добавлена")

@admin_router.put("/Models")
def put_Models(Models_info:Models_model, role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT code_model FROM Models WHERE code_model = {Models_info.code_model};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Модель с таким кодом не найдена"})

    if (Models_info.name == ""):
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})
    # Обновление данных о работнике
    cursor.execute(f'''
        UPDATE Models
        SET name = "{Models_info.name}",
            id_goods = "{Models_info.id_goods}",
            model_price = "{Models_info.model_price}"
        WHERE code_model = {Models_info.code_model};
    ''')
    conn.commit()
    conn.close()
    return {"message": f"Данные модели с кодом {Models_info.code_model} успешно обновлены"}

@admin_router.delete("/Models")
def delete_Models(Models_info:Models_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT code_model FROM Models WHERE code_model = {Models_info.code_model};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Модель с таким кодом не найдена"})

    # Удаление данных о работнике
    cursor.execute(f'DELETE FROM Models WHERE code_model = {Models_info.code_model};')
    conn.commit()
    conn.close()
    return {"message": f"Данные о модели с кодом {Models_info.code_model} успешно удалены"}

@admin_router.post("/Workers")
def post_Workers(Workers_info:Workers_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT id_worker FROM Workers WHERE
        id_worker = {Workers_info.id_worker};
    ''')
    data = cursor.fetchall()
    print(data)
    if len(data)!=0:
        return JSONResponse(status_code=404, content={"message": "Кладовщик с таким кодом уже существует"})
    if Workers_info.full_name == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})
    if is_valid_phone_number(Workers_info.phone_num) != True:
        return JSONResponse(status_code=404, content={"message": "Неправильный формат ввода номера телефона: + 7 (xxx) xxx-xxxx"})
    cursor.execute(f'INSERT INTO Workers (id_worker, full_name) VALUES ({Workers_info.id_worker},"{Workers_info.full_name}")')
    conn.commit()
    conn.close()
    return("Кладовщик усепшно добавлен")

@admin_router.put("/Workers")
def put_Workers(Workers_info:Workers_model, role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT id_worker FROM Workers WHERE id_worker = {Workers_info.id_worker};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Помещение с таким кодом не найдено"})
    if Workers_info.full_name == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})
    if is_valid_phone_number(Workers_info.phone_num) != True:
        return JSONResponse(status_code=404, content={"message": "Неправильный формат ввода номера телефона: + 7 (xxx) xxx-xxxx"})

    # Обновление данных о работнике
    cursor.execute(f'''
        UPDATE Workers
        SET full_name = "{Workers_info.full_name}",
            phone_num = "{Workers_info.phone_num}"
        WHERE id_worker = {Workers_info.id_worker};
    ''')
    conn.commit()
    conn.close()
    return {"message": f"Данные Кладовщика с кодом {Workers_info.id_worker} успешно обновлены"}

@admin_router.delete("/Workers")
def delete_Workers(Workers_info:Workers_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT id_worker FROM Workers WHERE id_worker = {Workers_info.id_worker};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Помещение с таким кодом не найдено"})

    # Удаление данных о работнике
    cursor.execute(f'DELETE FROM Workers WHERE id_worker = {Workers_info.id_worker};')
    conn.commit()
    conn.close()
    return {"message": f"Данные о кладовщике с кодом {Workers_info.id_worker} успешно удалены"}

@admin_router.post("/Incomes")
def post_Incomes(Incomes_info:Incomes_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute(f'''
        SELECT id_income FROM Incomes WHERE
        id_income = {Incomes_info.id_income};
    ''')
    data = cursor.fetchall()
    print(data)
    if len(data)!=0:
        return JSONResponse(status_code=404, content={"message": "Товар с таким кодом уже существует"})
    if Incomes_info.id_income == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})
    cursor.execute(f'INSERT INTO Incomes (id_income, code_model, income_date, count, id_worker, id_room) VALUES ({Incomes_info.id_income},{Incomes_info.code_model},"{Incomes_info.income_date}",{Incomes_info.count},{Incomes_info.id_worker},{Incomes_info.id_room})')
    conn.commit()
    conn.close()
    return("Поступление усепшно добавлено")

@admin_router.put("/Incomes")
def put_Incomes(Incomes_info:Incomes_model, role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT id_income FROM Incomes WHERE id_income = {Incomes_info.id_income};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Помещение с таким кодом не найдено"})
    if Incomes_info.code_model == "":
        return JSONResponse(status_code=404, content={"message": "Пустое поле"})

    # Обновление данных о работнике
    cursor.execute(f'''
        UPDATE Incomes
        SET code_model = "{Incomes_info.code_model}",
            income_date = "{Incomes_info.income_date}",
            count = "{Incomes_info.count}",
            id_worker = "{Incomes_info.id_worker}",
            id_room = "{Incomes_info.id_room}"
        WHERE id_income = {Incomes_info.id_income};
    ''')
    conn.commit()
    conn.close()
    return {"message": f"Данные поступления с кодом {Incomes_info.id_income} успешно обновлены"}

@admin_router.delete("/Incomes")
def delete_Incomes(Incomes_info:Incomes_model,role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_admin(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})

    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()

    # Проверка существования работника с указанным ID
    cursor.execute(f'SELECT id_income FROM Incomes WHERE id_income = {Incomes_info.id_income};')
    data = cursor.fetchall()
    if len(data) == 0:
        return JSONResponse(status_code=404, content={"message": "Помещение с таким кодом не найдено"})

    # Удаление данных о работнике
    cursor.execute(f'DELETE FROM Incomes WHERE id_income = {Incomes_info.id_income};')
    conn.commit()
    conn.close()
    return {"message": f"Данные о кладовщике с кодом {Incomes_info.id_income} успешно удалены"}


def verify_admin(role) -> bool:
    if role == "admin":
        return True
    else:
        return False

def is_valid_phone_number(phone_number):
    # Регулярное выражение для проверки номера телефона
    pattern = re.compile(r'^\+\d{1,2}\s\(\d{3}\)\s\d{3}-\d{4}$')
    return bool(pattern.match(phone_number))
