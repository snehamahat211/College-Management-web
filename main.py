from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth import create_access_token, verify_token
from models import User, Student


app = FastAPI()

fake_user = {"username": "admin", "password": "admin123"}
students = []
