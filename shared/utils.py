"""
This module contains the authorizer function to validate the JWT token.
"""

import jwt
from fastapi import HTTPException, Request
from shared.constants import constants
from shared.application.services import AuthService


def get_user_authorizer(
    request: Request,
) -> dict:
    """
    Retrieves the user from the request's authorization token.

    Args:
        request (Request): The incoming request object.
        repository (Repository): The repository object used to retrieve the user.

    Returns:
        User: The authenticated user.

    Raises:
        HTTPException: If the token is expired or invalid, or if the user does not exist.
    """
    if "local" in constants.ENVIRONMENT_SAM.lower():
        token: str = request.headers.get("Authorization", "")
        from shared.application.services import AuthService
        from shared.utils import generate_policy_authorizer

        auth_service = AuthService()
        policy = generate_policy_authorizer({"authorizationToken": token}, auth_service)
        if policy["policyDocument"]["Statement"][0]["Effect"] == "Deny":
            raise HTTPException(status_code=401, detail="Unauthorized")
        return policy["context"]
    try:
        context = request.scope["aws.event"]["requestContext"]["authorizer"]
    except HTTPException as e:
        raise e
    return context


def generate_policy(principal_id, effect, data=None):
    """
    Genera una política de autorización para un recurso de Amazon API Gateway.

    :param principal_id: El ID del principal (usuario) al que se aplica la política.
    :type principal_id: str
    :param effect: El efecto de la política (Allow o Deny).
    :type effect: str
    :param data: Datos adicionales que se agregarán al contexto de la política.
    :type data: dict or None
    :return: La política de autorización generada.
    :rtype: dict
    """
    auth_response = {}
    auth_response["principalId"] = principal_id
    policy_document = {}
    policy_document["Version"] = "2012-10-17"
    policy_document["Statement"] = []
    statement_one = {}
    statement_one["Action"] = "execute-api:Invoke"
    statement_one["Effect"] = effect
    statement_one["Resource"] = "*"
    policy_document["Statement"].append(statement_one)
    auth_response["policyDocument"] = policy_document
    auth_response["context"] = data or {}

    return auth_response


def generate_policy_authorizer(event: dict, auth_service: AuthService):
    if not event or not event.get("authorizationToken"):
        return generate_policy("user", "Deny")
    token = event.get("authorizationToken")
    token_decode = jwt.decode(jwt=token, key=constants.SECRET_KEY, algorithms=["HS256"])
    user_id = auth_service.get_user_by_uuid(token_decode["uuid"])
    if user_id:
        return generate_policy(user_id, "Allow", token_decode)
    return generate_policy("user", "Deny")
