from domain_auth.entities import User
from domain_auth.repositories import UserRepository
from shared.infrastructure.dynamodb_repository import DynamoDBRepository
from boto3.dynamodb.conditions import Key


class DynamoDBUserRepository(DynamoDBRepository, UserRepository):
    def save(self, user: User) -> User:
        item = {
            "PK": f"USER",
            "SK": f"{user.user_id}",
            "username": user.username,
            "password": user.password,
            "phone": user.phone,
            "first_name": user.first_name,
        }
        self.put_item(item)
        return user

    def find_by_id(self, user_id: str) -> User:
        item: dict = self.get_item(f"USER", user_id)
        if item:
            return User(
                user_id=user_id,
                name=item["username"],
                first_name=item.get("first_name"),
                phone=item.get("phone"),
                password=item.get("password"),
                address=item.get("address"),
            )
        return None

    def find_by_username(self, username: str) -> User:
        query_kwargs = {
            "KeyConditionExpression": Key("PK").eq("USER")
            & Key("username").eq(username)
        }
        response = self.table.query(**query_kwargs)
        items = response.get("Items", [])
        if items:
            item = items[0]
            return User(
                user_id=item["SK"],
                name=item["username"],
                first_name=item.get("first_name"),
                phone=item.get("phone"),
                password=item.get("password"),
                address=item.get("address"),
            )
        return None
