import datetime

from pydantic import BaseModel, Field
class Goods_model(BaseModel):
    id_goods:int
    name:str
class Models_model(BaseModel):
    code_model:int
    name:str
    id_goods:int
    model_price:float

class Incomes_model(BaseModel):
    id_income: int
    code_model: int
    income_date: datetime.date
    count: int
    id_worker: int
    id_room: int

class Workers_model(BaseModel):
    id_worker: int
    full_name: str
    phone_num: str

class Rooms_model(BaseModel):
    id_room: int
    type_room:str