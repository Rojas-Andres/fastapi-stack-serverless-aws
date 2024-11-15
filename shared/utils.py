"""
This module contains the authorizer function to validate the JWT token.
"""

import jwt
from fastapi import HTTPException, Request
from shared.constants import constants


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
    token: str = request.headers.get("Authorization", "")
    if (
        "local" in constants.ENVIRONMENT.lower()
        or "dev" in constants.ENVIRONMENT.lower()
    ):
        from src.authorizer.app import handler

        event = {
            "authorizationToken": token,
        }
        context = handler(event, {})
        if not context["context"]:
            raise HTTPException(status_code=401, detail="Unauthorized")
        return context["context"]
    try:
        context = request.scope["aws.event"]["requestContext"]["authorizer"]
    except HTTPException as e:
        raise e
    return context
