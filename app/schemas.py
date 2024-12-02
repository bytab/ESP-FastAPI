from pydantic import BaseModel

# Schema for updating an item
class ItemUpdate(BaseModel):
    id: int
    name: str = None
    description: str = None
    manufacturer: str = None
    price: str = None
    additional_info: str = None
