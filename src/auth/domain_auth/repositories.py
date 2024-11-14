from abc import ABC, abstractmethod
from domain_auth.entities import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User: ...

    @abstractmethod
    def find_by_id(self, user_id: str) -> User: ...

    @abstractmethod
    def find_by_username(self, username: str) -> User: ...
