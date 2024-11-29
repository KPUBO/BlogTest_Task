import logging

import uvicorn
from fastapi import FastAPI

from routers.posts import router as posts_router

app = FastAPI()

app.include_router(posts_router, prefix="/posts", tags=["posts"])

logger = logging.getLogger("uvicorn")

@app.on_event("startup")
async def startup_event():
    logger.info("Documentation: http://127.0.0.1:8000/docs")
@app.get("/")
def read_root():
    return {"message": "Hello, Complex World!"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)