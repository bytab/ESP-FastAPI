from fastapi import WebSocket, WebSocketDisconnect

# WebSocket connection manager
class WebSocketManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}

    async def connect(self, websocket: WebSocket, esp_id: int):
        await websocket.accept()
        self.active_connections[esp_id] = websocket

    def disconnect(self, esp_id: int):
        self.active_connections.pop(esp_id, None)

    async def send_to_esp(self, esp_id: int, message: dict):
        websocket = self.active_connections.get(esp_id)
        if websocket:
            await websocket.send_json(message)
