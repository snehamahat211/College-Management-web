from sqlmodel import SQLModel, Field
from typing import Optional

class User(SQLModel):
    username: str
    password: str

class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    age: int
    grade: str
