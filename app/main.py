import uvicorn
from fastapi import FastAPI

from app.database.db import Base, engine
from app.routes.auth_routes import auth_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
