from pathlib import Path

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

import sys
import requests

from python_tools.fastapi.web_response import WebMessage

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)


class DisableCacheMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response


app.add_middleware(DisableCacheMiddleware)


@app.get("/")
def get_root():
    return "Hello, World!"

@app.get("/v1")
def get_root():
    print_imports_paths()
    return WebMessage().return_text()

@app.get("/v2")
def get_root():
    sys.path.insert(0, "/Users/sundaram/temp/python-tools/src")
    sys.path.insert(0, "/Users/sundaram/temp/python-tools/src/python_tools/fastapi")
    print_imports_paths()
    return WebMessage().return_text()


def run():
    ssl_keyfile = "/path/to/ssl.key"
    ssl_certfile = "/path/to/ssl.cert"
    config = uvicorn.Config(app, host="0.0.0.0", port=8080, reload=False, log_level="debug",
                            workers=5)
    if Path(ssl_keyfile).exists() and Path(ssl_certfile).exists():
        config = uvicorn.Config(app, host="0.0.0.0", port=8080, reload=False, log_level="debug",
                                workers=5, ssl_keyfile=ssl_keyfile,
                                ssl_certfile=ssl_certfile)

    server = uvicorn.Server(config)
    server.run()


def print_imports_paths():
    for idx, path in enumerate(sys.path, 1):
        print(f'{idx} - {path}')

    print(f'\nrequests module location - {requests.__file__}')


if __name__ == "__main__":
    print_imports_paths()
    run()
