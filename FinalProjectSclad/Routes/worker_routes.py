from fastapi.responses import JSONResponse
from Authorization.authorization import KeycloakJWTBearerHandler, HTTPException
import sqlite3
from fastapi import APIRouter, Depends
import json
worker_router = APIRouter(
    tags=["Employeer"]
)

@worker_router.get("/Goods_w")
def get_Goods(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_worker(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Goods;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@worker_router.get("/Models_w")
def get_Models(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_worker(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Models;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@worker_router.get("/Incomes_w")
def get_Incomes(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_worker(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Incomes;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@worker_router.get("/Workers_w")
def get_Workers(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_worker(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Workers;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

@worker_router.get("/Rooms_w")
def get_Rooms(role=Depends(KeycloakJWTBearerHandler())):
    # Проверка авторизации
    if not verify_worker(role):
        raise HTTPException(status_code=403, detail={"message": "Доступ запрещен"})
    conn = sqlite3.connect('C:\\Users\\maks_\\PycharmProjects\\FinalProjectSclad\\Database\\sclad.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM Rooms;
    ''')
    result = json.loads(json.dumps(cursor.fetchall()))
    conn.close()
    return result

def verify_worker(role) -> bool:
    if role == "worker":
        return True
    else:
        return False