from decimal import Decimal
from sqlite3 import Date

from pydantic import EmailStr
from unicodedata import name
from ninja import Schema
from typing import List
from pydantic import BaseModel

class ProductOut(Schema):
    name: str
    #weight: float = None
    price: int
    description: str = None
    image: str
    

class CustomerOut(Schema):
    name:str
    email:EmailStr
    
class Favorites(Schema):
    customer:CustomerOut
    product: ProductOut
    feature:bool
    
class FourOFourOut(Schema):
    detail: str