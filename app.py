from fastapi import FastAPI
from fastapi.responses import FileResponse
from typing import Union # Import Union for type hinting float or None

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
async def train(text: str): # Explicitly type hint text as string
    game.train(text)
    return {"message": "Training complete"} # Return a response for the client


@app.get("/gen_message")
async def gen_message(message: str, energy: Union[float, None] = 0.8): # Explicitly type hint energy as float
    # Ensure energy is a float, defaulting if it somehow comes as None
    if energy is None:
        energy = 0.8
    return game.gen_message(message, energy)
