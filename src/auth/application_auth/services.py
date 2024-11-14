import uuid

from domain_auth.entities import User
from domain_auth.exceptions import UserNotFoundException, UserAlreadyExistsException
from infrastructure_auth.dynamodb_user_repository import (
    DynamoDBUserRepository,
)
from typing import List, Dict, Any, Optional
import json
from shared.infrastructure.database import table
from shared.encription import Hasher


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
