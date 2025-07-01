from fastapi import FastAPI
from fastapi.responses import FileResponse

from main import ProtoLLM

game = ProtoLLM()
app = FastAPI()


@app.get("/")
async def get_ui():
    return FileResponse("index.html")


@app.get("/styles.css")
async def get_styles():
    return FileResponse("styles.css")


@app.get("/script.js")
async def get_script():
    return FileResponse("script.js")


@app.post("/train")
async def train(text):
    game.train(text)


@app.get("/gen_message")
async def gen_message(message, energy=0.8):
    return game.gen_message(message, energy)
