"""
Execute this file to run the server local
"""

import configparser
import sys

import uvicorn
from fastapi import FastAPI, Request

config = configparser.ConfigParser()

config.read("config.ini")

for key, value in config.items("pythonpath"):
    sys.path.append(value)

from dotenv import load_dotenv

load_dotenv(dotenv_path=".env")
from fastapi.middleware.cors import CORSMiddleware

from src.auth.app import router as auth_router
from fastapi.responses import JSONResponse

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

from shared.logs.infrastructure.dynamodb_log_repository import DynamoDBLogRepository
from shared.infrastructure.database import table_logs
from shared.logs.application.services import LogService

log_repository = DynamoDBLogRepository(table_logs)
log_service = LogService(log_repository)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    # Obtenemos la URL y los parámetros
    url = str(request.url)
    params = dict(request.query_params)

    # Obtenemos el cuerpo de la solicitud si está disponible
    try:
        request_body = await request.json()
    except:
        request_body = None

    # Llamamos al siguiente middleware o al endpoint y capturamos la respuesta
    response = await call_next(request)
    status_code = response.status_code

    response_body = None
    if isinstance(response, JSONResponse):
        response_body = response.body.decode("utf-8")
    else:
        response_body = b"".join(
            [chunk async for chunk in response.body_iterator]
        ).decode("utf-8")

    log_service.log_response(
        api=request.scope["path"],
        status_code=status_code,
        response_body=response_body,
        request_body=request_body,
        params=params,
        url=url,
    )

    return response


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
