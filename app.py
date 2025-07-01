from fastapi import FastAPI, Body # Import Body for explicit request body parsing
from fastapi.responses import FileResponse
from typing import Union

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
async def train(text: str = Body(..., embed=True)): # Expect 'text' in the request body as JSON
    """
    Trains the ProtoLLM with the provided text.
    The text is expected in the request body as a JSON object, e.g., {"text": "Your training data here"}.
    """
    game.train(text)
    return {"message": "Training complete"}


@app.get("/gen_message")
async def gen_message(message: str, energy: Union[float, None] = 0.8):
    """
    Generates a message from the ProtoLLM based on a prompt and energy level.
    Message is a query parameter. Energy is an optional float query parameter.
    """
    # Ensure energy is a float, defaulting if it somehow comes as None
    if energy is None:
        energy = 0.8
    return game.gen_message(message, energy)
