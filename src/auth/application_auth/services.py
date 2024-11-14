import uuid

from domain_auth.entities import User
from domain_auth.exceptions import UserNotFoundException, UserAlreadyExistsException
from infrastructure_auth.dynamodb_user_repository import (
    DynamoDBUserRepository,
)
from typing import List, Dict, Any, Optional
import json
from shared.infrastructure.database import table


class UserService:
    def __init__(self):
        self.repository_user = DynamoDBUserRepository(table)

    def create_user(
        self, username: str, password: str, address: str, phone: str, first_name: str
    ) -> User:

        user_exists = self.repository_user.find_by_username(username)
        if user_exists:
            raise UserAlreadyExistsException(f"User with username {username} already exists.")
        
        company = User(
            company_id=str(uuid.uuid4()),
            username=username,
            password=password,
            address=address,
            phone=phone,
            first_name=first_name,
        )
        return self.repository_user.save(company)
