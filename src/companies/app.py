"""
Módulo que contiene la aplicación FastAPI que maneja las rutas de autenticación.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from presentation.company_controller import router as company_router
from starlette.requests import Request

from shared.infrastructure.database import table_logs
from shared.logs.application.services import LogService
from shared.logs.infrastructure.dynamodb_log_repository import DynamoDBLogRepository

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Company Service",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

log_repository = DynamoDBLogRepository(table_logs)
log_service = LogService(log_repository)


@app.middleware("http")
async def log_requests(request: Request, call_next):
    url = str(request.url)
    params = dict(request.query_params)

    try:
        request_body = await request.json()
    except:
        request_body = None

    response = await call_next(request)
    status_code = response.status_code

    response_body = None
    try:
        if hasattr(response, "body"):
            response_body = response.body.decode("utf-8")
        elif hasattr(response, "body_iterator"):
            chunks = [chunk async for chunk in response.body_iterator]
            response_body = b"".join(chunks).decode("utf-8")

            async def new_body_iterator():
                for chunk in chunks:
                    yield chunk

            response.body_iterator = new_body_iterator()
    except Exception as e:
        response_body = f"Error al leer el cuerpo de la respuesta: {e}"
    log_service.log_response(
        api=request.scope["path"],
        status_code=status_code,
        response_body=response_body,
        request_body=request_body,
        params=params,
        url=url,
    )

    return response


app.include_router(company_router)
handler = Mangum(app)
