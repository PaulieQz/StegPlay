from fastapi import FastAPI, File, UploadFile, Form, BackgroundTasks
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from PIL import Image
import shutil
import os
import time
from .steganography import embed_message, extract_message

app = FastAPI()

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return templates.TemplateResponse("index.html", {"request": {}})

@app.post("/encrypt", response_class=FileResponse)
async def encrypt_image(message: str = Form(...), file: UploadFile = File(...)):
    temp_file_path = f"app/static/temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    stego_image = embed_message(temp_file_path, message)
    stego_image_path = f"app/static/stego_{file.filename}"
    stego_image.save(stego_image_path)

    return stego_image_path

@app.post("/decrypt", response_class=HTMLResponse)
async def decrypt_image(file: UploadFile = File(...)):
    temp_file_path = f"app/static/temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    secret_message = extract_message(temp_file_path)

    return templates.TemplateResponse("decrypt_result.html", {"request": {}, "message": secret_message})

@app.get("/progress")
async def get_progress():
    def event_generator():
        for progress in range(0, 101, 10):
            yield f"data:{progress}\n\n"
            time.sleep(1)
        yield f"data:complete\n\n"

    return StreamingResponse(event_generator(), media_type="text/event-stream")
