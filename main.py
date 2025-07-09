from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import select, Session
from auth import create_access_token, verify_token
from database import get_session, engine
from models import User, Student, SQLModel

app = FastAPI()

# Create tables on startup
@app.on_event("startup")
def startup():
    SQLModel.metadata.create_all(engine)

# Static single-user auth (from .env)
fake_user = {"username": "admin", "password": "admin123"}
students = []

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username == fake_user["username"] and form_data.password == fake_user["password"]:
        token = create_access_token(data={"sub": form_data.username})
        return {"access_token": token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
@app.post("/students", dependencies=[Depends(verify_token)])
def add_student(student: Student, session: Session = Depends(get_session)):
    session.add(student)
    session.commit()
    session.refresh(student)
    return {"message": "Student added", "data": student}

@app.get("/students", dependencies=[Depends(verify_token)])
def get_students(session: Session = Depends(get_session)):
    students = session.exec(select(Student)).all()
    return students
