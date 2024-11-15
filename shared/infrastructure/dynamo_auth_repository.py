from boto3.dynamodb.conditions import Key
from shared.domain.entities import Auth

from shared.domain.repositories import AuthRepository

from shared.infrastructure.dynamodb_repository import DynamoDBRepository


class DynamoDBAuthRepository(AuthRepository):
    def __init__(self, table):
        self.table = table

    def get_item(self, uuid: str) -> dict:
        response = self.table.get_item(Key={"uuid": uuid})
        return response.get("Item")

    def put_item(self, item: dict):
        self.table.put_item(Item=item)

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

    def delete(self, uuid: str):
        self.table.delete_item(Key={"uuid": uuid})
