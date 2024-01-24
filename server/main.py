from fastapi import FastAPI

from server.api import router
from fastapi.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    application = FastAPI()

    api_prefix = "/api"

    application.include_router(router, prefix=api_prefix)

    return application


app = get_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

