"""
Este módulo contiene la función de controlador para autorizar y validar tokens de acceso en una función Lambda.
"""

import os
import traceback

import jwt
from shared.application.services import AuthService
from shared.utils import generate_policy_authorizer, generate_policy

auth_service = AuthService()


def handler(event, context):
    """
    Función de controlador para autorizar y validar tokens de acceso en una función Lambda.

    Esta función maneja la autorización y validación de tokens de acceso en el contexto de una función Lambda.
    Verifica la presencia y validez del token de autorización en el evento proporcionado. Si el token es válido,
    genera una política de autorización con permisos adecuados y devuelve la política. Si el token no es válido
    o está ausente, genera una política que deniega el acceso.

    :param event: Los datos del evento recibido por la función Lambda.
    :type event: dict
    :param context: El contexto de la función Lambda.
    :type context: LambdaContext
    :return: Una política de autorización generada con permisos adecuados o denegando el acceso.
    :rtype: dict
    """
    try:
        policy = generate_policy_authorizer(event, auth_service)
        return policy
    except jwt.exceptions.DecodeError:
        print(traceback.format_exc())
        return generate_policy("user", "Deny")
    except Exception as e:
        print(traceback.format_exc())
        return generate_policy("user", "Deny", str(e))
