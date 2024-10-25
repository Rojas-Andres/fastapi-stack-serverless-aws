"""
Módulo que contiene la aplicación FastAPI que maneja las rutas de autenticación.
"""

import os

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum
from presentation.company_controller import router as company_router

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
app.include_router(company_router)
handler = Mangum(app)
