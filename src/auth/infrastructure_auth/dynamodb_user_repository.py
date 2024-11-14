from domain_auth.entities import User
from domain_auth.repositories import UserRepository
from shared.infrastructure.dynamodb_repository import DynamoDBRepository
from boto3.dynamodb.conditions import Key
from domain_auth.exceptions import UserAlreadyExistsException


class DynamoDBUserRepository(DynamoDBRepository, UserRepository):
    def save(self, user: User) -> User:
        item = {
            "PK": f"USER",
            "SK": f"{user.user_id}",
            "username": user.username,
            "password": user.password,
            "phone": user.phone,
            "first_name": user.first_name,
            "email": user.email,
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

    def find_by_email(self, email: str) -> User:
        query_kwargs = {
            "IndexName": "GSI_Email",  # Nombre del índice que usa email como clave de partición
            "KeyConditionExpression": Key("email").eq(email),
        }
        response = self.table.query(**query_kwargs)
        items = response.get("Items", [])
        if items:
            raise UserAlreadyExistsException(f"User with email {email} already exists.")
        return None
