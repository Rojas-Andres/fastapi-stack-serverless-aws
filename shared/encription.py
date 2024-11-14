"""
Archivo que contiene la clase Hasher, la cual proporciona métodos para trabajar con contraseñas y hashes.
"""

import time

import jwt
from passlib.context import CryptContext
from shared.constants import constants

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class Hasher:
    """
    Esta clase proporciona métodos para trabajar con contraseñas y hashes.
    """

    @staticmethod
    def verify_password(plain_password, hashed_password):
        """
        Verifica si una contraseña en texto plano coincide con su versión hasheada.

        :param plain_password: La contraseña en texto plano que se va a verificar.
        :type plain_password: str
        :param hashed_password: La versión hasheada de la contraseña almacenada.
        :type hashed_password: str
        :return: True si la contraseña coincide, False si no coincide.
        :rtype: bool
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def get_password_hash(password: str):
        """
        Genera un hash a partir de una contraseña en texto plano.

        :param password: La contraseña en texto plano que se va a hashear.
        :type password: str
        :return: El hash resultante de la contraseña.
        :rtype: str
        """
        return pwd_context.hash(password)


def generate_token(uuid: str) -> str:
    """
    Generates a JWT token with the given UUID and an expiration time.

    Args:
        uuid (str): The UUID to include in the token payload.

    Returns:
        str: The encoded JWT token as a string.
    """

    data = {}
    expires_at: int = int(time.time()) + constants.TOKEN_API_EXPIRATION
    data["expires_at"] = expires_at
    data["uuid"] = uuid
    encode_data: str = jwt.encode(
        payload=data, key=constants.SECRET_KEY, algorithm="HS256"
    )
    return encode_data
