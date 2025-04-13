from fastapi import FastAPI
import uvicorn
from fastapi.responses import RedirectResponse


app = FastAPI(title="Task Manager")

@app.get("/")
async def redirect_swagger():
    return RedirectResponse("/docs")


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port = 8088, reload=True)