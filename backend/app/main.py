import uvicorn
from fastapi import FastAPI

from app.core import config
from app.core.celery_app import celery_app
from app import tasks


app = FastAPI(
    docs_url="/api/docs",
    openapi_url="/api",
)

@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}

@app.get("/api/v1/task")
async def example_task():
    celery_app.send_task("app.tasks.example_task", args=["Hello World"])

    return {"message": "success"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8888)
