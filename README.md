# ESP-FastAPI Baga-ESL Project 

This project demonstrates how to connect an **ESP32** device to a backend API using **FastAPI** with **WebSockets**. The backend allows real-time updates for product prices, names, descriptions, manufacturers, and other information, which can be displayed on an ESP32-connected display. The project uses **FastAPI** as the backend server, **SQLAlchemy** for database management, and **WebSockets** for communication between the frontend (ESP32) and the backend.

## Features

- **WebSocket Communication**: Real-time data updates between the ESP32 and the backend.
- **FastAPI Backend**: The backend API is built using FastAPI for fast and efficient performance.
- **Database Integration**: SQLAlchemy is used to manage and query product information from the database.
- **ESP32 Integration**: The ESP32 device connects to the backend over Wi-Fi and receives updates for the product data displayed on a screen.
- **Easy Setup**: The project includes all necessary dependencies and instructions to get started quickly.

## Technologies Used

- **FastAPI**: Modern, fast (high-performance) web framework for building APIs.
- **Uvicorn**: ASGI server used to run the FastAPI application.
- **SQLAlchemy**: SQL toolkit and ORM used for database operations.
- **Websockets**: For real-time communication between the ESP32 and the backend.
- **ESP32**: Microcontroller used to display product data on a connected display.
- **Python 3.x**: Programming language used for the backend.

## Requirements

To run this project locally, you'll need:

- Python 3.7+ (preferably the latest version)
- **pip** (Python package manager)
- **virtualenv** (recommended for managing Python environments)

## Setup Instructions

### 1. Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/ESP-FastAPI.git
cd ESP-FastAPI
```

### 2. Create a Virtual Environment

Create a virtual environment to isolate your project dependencies:
```bash
python3 -m venv .venv
```
Activate the virtual environment:

On macOS/Linux:
```bash
source .venv/bin/activate
```
On Windows:
```bash
.venv\Scripts\activate
```

### 3. Install Dependencies
Install the required dependencies listed in the requirements.txt file:
```bash
pip install -r requirements.txt
```
### 4. Run the FastAPI Server
Start the FastAPI server using uvicorn:
```bash
uvicorn app.main:app --reload
```
### 5. Connect ESP32 to WebSocket
Connect your ESP32 to the server via Wi-Fi. The ESP32 should be set up to listen for updates on the WebSocket, and it will receive the product data dynamically as it's pushed from the server.

The WebSocket connection URL is:
```bash
ws://127.0.0.1:8000/ws/
```
Ensure that your ESP32 is configured correctly to connect to this WebSocket endpoint.

### Project Structure
```bash
ESP-FastAPI/
├── app/
│   ├── __init__.py
│   ├── main.py            # FastAPI application entry point
│   ├── models.py          # Database models (if applicable)
│   └── websocket.py       # WebSocket handling logic
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```
### Troubleshooting

If you encounter any issues related to dependencies, try recreating your virtual environment and reinstalling dependencies.
If the WebSocket connection fails, make sure your ESP32 is on the same network as the server and the WebSocket endpoint URL is correctly configured.

If you're interested in this project, write to me and I'll help you. 

