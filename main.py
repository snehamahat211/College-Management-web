from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, verify_token
from models import User, Student


app = FastAPI()

fake_user = {"username": "admin", "password": "admin123"}
students = []
@app.post("/")
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == fake_user["username"] and form_data.password==fake_user["password"]:
        token=create_access_token(data={"sub":form_data.username})
        return {"access_token":token,"token_type":"Bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
@app.post("/students", dependencies=[Depends(verify_token)])
def add_student(student: Student):
    students.append(student)
    return {"message": "Student added", "data": student}
@app.get("/students", dependencies=[Depends(verify_token)])
def get_students():
    return students
