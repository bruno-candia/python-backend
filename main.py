from fastapi import FastAPI
from routes.UserRoute import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/api/user")

@app.get("/api/health", tags=["Health"])
async def health():
    return {
        "status": "OK"
    }
