from fastapi import APIRouter;

logs_router = APIRouter(
    prefix="/api/logs",
    tags=["logs"],
)

logs_router.get('/')
def list_files():
    return {"files": []}