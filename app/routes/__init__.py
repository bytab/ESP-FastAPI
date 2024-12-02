from fastapi import APIRouter
from app.routes import items

# Initialize router
router = APIRouter()

# Include item routes
router.include_router(items.router, prefix="/items", tags=["items"])
