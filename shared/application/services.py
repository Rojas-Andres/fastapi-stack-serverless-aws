from shared.infrastructure.dynamo_auth_repository import DynamoDBAuthRepository
from shared.infrastructure.database import table_auth
from shared.domain.entities import Auth

import uuid
from shared.encription import generate_token


class AuthService:
    def __init__(self):
        self.repository_auth = DynamoDBAuthRepository(table_auth)

    def create_auth_login(
        self,
        email: str,
    ) -> str:
        uuid_auth = str(uuid.uuid4())
        token = generate_token(uuid_auth)
        token_auth = Auth(
            uuid=uuid_auth,
            jwt=token,
            email=email,
        )
        self.repository_auth.save(token_auth)
        return token

    def get_user_by_uuid(self, uuid: str) -> Auth:
        return self.repository_auth.get_user_by_uuid(uuid)
