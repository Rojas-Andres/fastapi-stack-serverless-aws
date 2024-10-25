"""
Execute this file to run the server local
"""

import configparser
import sys

import uvicorn
from fastapi import FastAPI

config = configparser.ConfigParser()

config.read("config.ini")

for key, value in config.items("pythonpath"):
    sys.path.append(value)

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
from fastapi.middleware.cors import CORSMiddleware

from src.auth.app import router as auth_router

# from src.user.app import router as user_router
from src.companies.presentation.company_controller import router as company_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # max_age=3600,
)


@app.options("/{path:path}")
async def options_handler(request, response, path):
    response.headers["Access-Control-Allow-Origin"] = request.headers.get("Origin", "*")
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PATCH"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return {"message": "ok"}


app.include_router(auth_router)
app.include_router(company_router)

if __name__ == "__main__":
    uvicorn.run("local:app", port=8002, reload=True)
