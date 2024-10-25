from fastapi import APIRouter, HTTPException
from application.services import CompanyService
from fastapi import status as response_status
from starlette.requests import Request
from companies.domain.exceptions import CompanyNotFoundException

router = APIRouter(prefix="/companies")

company_service = CompanyService()


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


@router.post("/")
def api_create_company(request: Request, name: str, address: str):
    return company_service.create_company(name, address)


@router.get("/{company_id}")
def api_get_company(request: Request, company_id: str):
    try:
        return company_service.get_company(company_id)
    except CompanyNotFoundException:
        raise HTTPException(status_code=404, detail="Company not found")


@router.patch("/{company_id}")
def api_update_company(request: Request, company_id: str, name: str, address: str):
    return company_service.update_company(company_id, name, address)


@router.delete("/{company_id}")
def api_delete_company(request: Request, company_id: str):
    company_service.delete_company(company_id)
    return {"message": "Company deleted"}
