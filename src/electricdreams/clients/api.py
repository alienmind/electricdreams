import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse

import electricdreams as ed

app = FastAPI(title="Electricdreams API")
painter = ed.Painter()
conversation = ed.Conversation()


@app.get("/image/")
async def get_image(prompt: str) -> FileResponse:
    ret = painter.paint(prompt)
    return FileResponse(ret)


@app.get("/query/")
async def query(prompt: str) -> str:
    ret = conversation.query(prompt)
    return ret


def run():
    """Launched with `poetry run electricdreams-api` at root level"""
    uvicorn.run("electricdreams.clients.api:app", host="0.0.0.0", port=8000, reload=True)
