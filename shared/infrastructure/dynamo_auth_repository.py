from boto3.dynamodb.conditions import Key
from shared.domain.entities import Auth

from domain.repositories import AuthRepository

from shared.infrastructure.dynamodb_repository import DynamoDBRepository


class DynamoDBAuthRepository(DynamoDBRepository, AuthRepository):
    def get_item(self, uuid: str, sk: str = None) -> dict:
        response = self.table.get_item(Key={"uuid": uuid})
        return response.get("Item")

    def save(self, auth: Auth) -> Auth:
        item = {
            "uuid": auth.uuid,
            "email": auth.email,
            "jwt": auth.jwt,
        }
        self.put_item(item)
        return auth

    def get_user_by_uuid(self, uuid: str) -> Auth:
        item: dict = self.get_item(uuid)
        if item:
            return Auth(
                uuid=uuid,
                email=item["email"],
                jwt=item["jwt"],
            )
        return None
