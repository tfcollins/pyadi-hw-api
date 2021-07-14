from api.routes import jif
from fastapi import APIRouter

router = APIRouter()
router.include_router(jif.router, tags=["jif"], prefix="/v1")
