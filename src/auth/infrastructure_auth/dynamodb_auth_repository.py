from boto3.dynamodb.conditions import Key
from domain_auth.entities import Auth, UserCommon
from domain_auth.exceptions import UserAlreadyExistsException
from domain_auth.repositories import AuthRepository

from shared.infrastructure.dynamodb_repository import DynamoDBRepository


class DynamoDBAuthRepository(DynamoDBRepository, AuthRepository):
    def save(self, auth: Auth) -> Auth:
        item = {
            "uuid": auth.uuid,
            "email": auth.email,
            "jwt": auth.jwt,
        }
        self.put_item(item)
        return auth
