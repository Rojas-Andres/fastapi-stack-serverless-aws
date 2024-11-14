from boto3.dynamodb.conditions import Key
from domain_auth.entities import User, UserCommon
from domain_auth.exceptions import UserAlreadyExistsException
from domain_auth.repositories import UserRepository

from shared.infrastructure.dynamodb_repository import DynamoDBRepository


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
            "address": user.address,
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
        """
        Find a user by their email address.

        Args:
            email (str): The email address of the user to find.

        Returns:
            User: The user object if found.
            bool: False if no user is found with the given email.
        """
        query_kwargs = {
            "IndexName": "GSI_Email",
            "KeyConditionExpression": Key("email").eq(email),
        }
        response = self.table.query(**query_kwargs)
        items = response.get("Items", [])
        if not items:
            return False
        return User(
            user_id=items[0]["SK"],
            username=items[0]["username"],
            password=items[0]["password"],
            address=items[0]["address"],
            phone=items[0]["phone"],
            first_name=items[0]["first_name"],
            email=email,
        )
