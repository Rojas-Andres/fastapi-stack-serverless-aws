"""
Módulo que contiene la aplicación FastAPI que maneja las rutas de autenticación.
"""

import os

from fastapi import APIRouter, Depends, FastAPI, HTTPException
from fastapi import status as response_status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from mangum import Mangum
from starlette.requests import Request

app = FastAPI(
    debug=os.getenv("DEBUG", False),
    title="Auth Service",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter(prefix="/auth")


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    """
    Maneja las excepciones de validación que ocurren al procesar una solicitud HTTP en FastAPI.

    :param request: La solicitud HTTP que causó la excepción.
    :type request: Request
    :param exc: La excepción de validación que fue capturada.
    :type exc: RequestValidationError
    :return: Una respuesta JSON que describe los errores de validación y el contenido de la solicitud.
    :rtype: JSONResponse
    """
    return JSONResponse(
        status_code=response_status.HTTP_400_BAD_REQUEST,
        content=jsonable_encoder({"errors": exc.errors(), "body": exc.body}),
    )


@router.post(
    "/signup",
    status_code=response_status.HTTP_201_CREATED,
)
async def singup(request: Request):
    """
    Registra un nuevo usuario en el sistema.

    :param request: La solicitud HTTP recibida.
    :type request: Request
    :param user: Los datos del usuario a ser registrados.
    :param db: Una sesión de base de datos.
    :type db: Session
    :return: Una respuesta que indica el éxito del registro.
    :rtype: dict
    """
    return {"response": "User create ok"}


@router.post(
    "/signin",
    status_code=response_status.HTTP_200_OK,
)
async def signin(
    request: Request,
):
    """
    Permite que un usuario inicie sesión en el sistema.

    :param request: La solicitud HTTP recibida.
    :type request: Request
    :param credentials: Las credenciales de inicio de sesión proporcionadas por el usuario.
    :param db: Una sesión de base de datos.
    :type db: Session
    :return: Una respuesta que indica el éxito del inicio de sesión.
    :rtype: dict
    """
    return {"response": "User signin ok"}


@router.get(
    "/health",
    status_code=response_status.HTTP_200_OK,
)
async def api_health(
    request: Request,
):
    """
    Permite que un usuario inicie sesión en el sistema.

    :param request: La solicitud HTTP recibida.
    :type request: Request
    :param credentials: Las credenciales de inicio de sesión proporcionadas por el usuario.
    :param db: Una sesión de base de datos.
    :type db: Session
    :return: Una respuesta que indica el éxito del inicio de sesión.
    :rtype: dict
    """
    return {"response": "Service is ok"}


app.include_router(router)
handler = Mangum(app)
