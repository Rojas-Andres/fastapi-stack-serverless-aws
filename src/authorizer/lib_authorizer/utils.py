"""
Este módulo contiene funciones de utilidad para el módulo authorizer.
"""


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
