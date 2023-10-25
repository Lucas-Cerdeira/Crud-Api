from fastapi import FastAPI

from routes import root_router, user_router



app = FastAPI()
app.include_router(root_router.router)
app.include_router(user_router.router)
