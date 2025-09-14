# fastapi_service/app/main.py

from fastapi import FastAPI
from fastapi_service.app.config.database import Base, engine
from fastapi_service.app.routes import post_routes

# Create tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="FastAPI Service")

# Register routes
app.include_router(post_routes.router)
