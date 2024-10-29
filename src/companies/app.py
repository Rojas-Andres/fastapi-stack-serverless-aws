"""
Módulo que contiene la aplicación FastAPI que maneja las rutas de autenticación.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from presentation.company_controller import router as company_router
from starlette.requests import Request
import uuid
from datetime import datetime

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


def clean_sensitive_data(data, sensitive_keys=None):
    if sensitive_keys is None:
        sensitive_keys = {
            "password",
            "secret",
            "token",
            "access_token",
            "refresh_token",
        }

    def _clean(item):
        if isinstance(item, dict):
            return {
                k: _clean(v) if k not in sensitive_keys else "REDACTED"
                for k, v in item.items()
            }
        elif isinstance(item, list):
            return [_clean(i) for i in item]
        return item

    return _clean(data)


@app.middleware("http")
async def log_request_and_response(request: Request, call_next):
    request_id = str(uuid.uuid4())
    method = request.method
    url = str(request.url)
    headers = dict(request.headers)
    query_params = dict(request.query_params)

    try:
        body = (
            await request.json() if request.method in ["POST", "PUT", "PATCH"] else {}
        )
        body = clean_sensitive_data(body)
    except Exception:
        body = {}

    response = await call_next(request)

    status_code = response.status_code
    response_body = await response.body()

    log_data = {
        "request_id": request_id,
        "timestamp": datetime.utcnow().isoformat(),
        "method": method,
        "url": url,
        "headers": headers,
        "query_params": query_params,
        "request_body": body,
        "status_code": status_code,
        "response_body": response_body.decode(
            "utf-8"
        ),  # Decodifica el cuerpo de la respuesta
    }

    try:
        table.put_item(Item=log_data)
    except Exception as e:
        print(f"Error guardando la solicitud y respuesta en DynamoDB: {e}")

    return response


app.include_router(company_router)
handler = Mangum(app)
