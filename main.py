from fastapi import FastAPI
from app.database import engine, Base
from app.routes import items

# Create all database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include routes
app.include_router(items.router)
