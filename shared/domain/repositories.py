from abc import ABC, abstractmethod
from shared.domain.entities import Auth


class AuthRepository(ABC):
    @abstractmethod
    def save(self, auth: Auth) -> Auth: ...

    @abstractmethod
    def get_user_by_uuid(self, uuid: str) -> Auth: ...
