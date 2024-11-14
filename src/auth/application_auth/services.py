import json
import uuid
from typing import Any, Dict, List, Optional

from domain_auth.entities import Auth, User, UserCommon
from domain_auth.exceptions import (
    UserAlreadyExistsException,
    ValidationError,
    UserPasswordInvalid,
)
from infrastructure_auth.dynamodb_auth_repository import DynamoDBAuthRepository
from infrastructure_auth.dynamodb_user_repository import DynamoDBUserRepository

from shared.encription import Hasher, generate_token
from shared.infrastructure.database import table, table_auth


class UserService:
    def __init__(self):
        self.repository_user = DynamoDBUserRepository(table)
        self.hasher = Hasher()

    def create_user(
        self,
        username: str,
        password: str,
        address: str,
        phone: str,
        first_name: str,
        email: str,
    ) -> User:
        user_exists = self.repository_user.find_by_email(email)
        if user_exists:
            raise UserAlreadyExistsException(f"User with email {email} already exists.")
        password_hash = self.hasher.get_password_hash(password)
        user = User(
            user_id=str(uuid.uuid4()),
            username=username,
            password=password_hash,
            address=address,
            phone=phone,
            first_name=first_name,
            email=email,
        )
        return self.repository_user.save(user)

    def validate_user_login(
        self,
        password: str,
        email: str,
    ) -> User:
        user_exists: User = self.repository_user.find_by_email(email)
        print("user: ", user_exists)
        if not user_exists:
            raise UserAlreadyExistsException(message="User does not exist")
        password_hash = self.hasher.verify_password(password, user_exists.password)
        if not password_hash:
            raise ValidationError(message="Password is invalid")
        return user_exists


class AuthService:
    def __init__(self):
        self.repository_auth = DynamoDBAuthRepository(table_auth)

    def create_auth_login(
        self,
        email: str,
    ) -> User:
        uuid_auth = str(uuid.uuid4())
        token = generate_token(uuid_auth)
        token_auth = Auth(
            uuid=uuid_auth,
            jwt=token,
            email=email,
        )
        self.repository_auth.save(token_auth)
        return token
