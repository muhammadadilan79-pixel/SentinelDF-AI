from fastapi import APIRouter

router = APIRouter()


@router.get("/health", tags=["System"])
def health():
    return {
        "status": "healthy",
        "service": "SentinelDF AI",
        "version": "0.0.1"
    }