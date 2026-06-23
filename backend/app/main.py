from fastapi import FastAPI

from app.routes.health import router as health_router
from app.routes.upload import router as upload_router

app = FastAPI(
    title="SentinelDF AI",
    description="AI-Powered Digital Forensics Investigation Platform",
    version="0.0.1"
)


@app.get("/", tags=["System"])
def home():
    return {
        "project": "SentinelDF AI",
        "version": "0.0.1",
        "status": "running"
    }


app.include_router(health_router)
app.include_router(upload_router)