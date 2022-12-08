from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn
import electricdreams as ed

app = FastAPI()
painter = ed.Painter()

@app.get("/image/")
async def get_image(prompt: str) -> FileResponse :
    ret = painter.paint(prompt)
    return FileResponse(ret)

def run():
    """Launched with `poetry run electricdreams-api` at root level"""
    uvicorn.run("electricdreams-api.api:app", host="0.0.0.0", port=8000, reload=True)
