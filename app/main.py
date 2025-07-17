from fastapi import FastAPI

from app.api.v1 import router

from app.db.db import init_db

init_db()

app = FastAPI()

app.include_router(router)

@app.get("/")
def read_root():
    return {"Hello": "World"}