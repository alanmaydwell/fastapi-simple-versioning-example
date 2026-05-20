import time
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def the_time():
    return time.strftime("%H:%M:%S")
