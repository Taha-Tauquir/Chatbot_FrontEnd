from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
async def serve_chat():
    return FileResponse("chat.html")
