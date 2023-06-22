from fastapi import FastAPI, HTTPException, status
from models.models import User, User_Update
from utils import validate
from router import root_router, user_router



app = FastAPI()
app.include_router(root_router.router, tags=['router'])
app.include_router(user_router.router, tags=['user'])


users = []
