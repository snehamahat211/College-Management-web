from pydantic import BaseModel

class User(BaseModel):
    username:str
    password:str

class Student(BaseModel):
    id:int
    name:str
    department:str
    