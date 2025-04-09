from fastapi import FastAPI
from controller.abb_controller import router

app = FastAPI()

app.include_router(router)
