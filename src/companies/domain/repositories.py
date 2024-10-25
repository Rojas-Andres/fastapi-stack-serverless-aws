from abc import ABC, abstractmethod
from domain.entities import Company


class CompanyRepository(ABC):
    @abstractmethod
    def save(self, company: Company) -> Company:
        pass

    @abstractmethod
    def find_by_id(self, company_id: str) -> Company:
        pass

    @abstractmethod
    def update(self, company: Company) -> Company:
        pass

    @abstractmethod
    def delete(self, company_id: str) -> None:
        pass
