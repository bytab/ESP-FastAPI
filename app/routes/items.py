from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Item
from app.schemas import ItemUpdate
from app.websocket_manager import WebSocketManager

# Router instance
router = APIRouter()

# WebSocket manager instance
websocket_manager = WebSocketManager()

@router.websocket("/ws/{esp_id}")
async def websocket_endpoint(websocket: WebSocket, esp_id: int):
    await websocket_manager.connect(websocket, esp_id)
    try:
        while True:
            data = await websocket.receive_text()
            print(f"Received from ESP {esp_id}: {data}")
    except WebSocketDisconnect:
        websocket_manager.disconnect(esp_id)
        print(f"ESP {esp_id} disconnected")

@router.post("/update-item/")
async def update_item(item: ItemUpdate, db: Session = Depends(get_db)):
    # Fetch item from the database
    db_item = db.query(Item).filter(Item.id == item.id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")

    # Update item fields
    if item.name:
        db_item.name = item.name
    if item.description:
        db_item.description = item.description
    if item.manufacturer:
        db_item.manufacturer = item.manufacturer
    if item.price:
        db_item.price = item.price
    if item.additional_info:
        db_item.additional_info = item.additional_info

    db.commit()

    # Notify the ESP32 via WebSocket
    await websocket_manager.send_to_esp(item.id, {
        "name": db_item.name,
        "description": db_item.description,
        "manufacturer": db_item.manufacturer,
        "price": db_item.price,
        "additional_info": db_item.additional_info,
    })

    return {"detail": "Item updated successfully"}
