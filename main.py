from fastapi import FastAPI
from routers import the_time
from routers import the_time_v2


app = FastAPI()

app.include_router(the_time.router, prefix="/now")
app.include_router(the_time.router, prefix="/v1/now")
app.include_router(the_time_v2.router, prefix="/v2/now")
app.include_router(the_time_v2.router, prefix="/latest/now")
