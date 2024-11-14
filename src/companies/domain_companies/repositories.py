from abc import ABC, abstractmethod
from typing import List, Optional, Tuple

from domain_companies.entities import Company


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

    @abstractmethod
    def get_companies_paginated(
        self, limit: int, last_evaluated_key: Optional[dict] = None
    ) -> Tuple[List[Company], Optional[dict]]:
        """
        Devuelve una lista de compañías y una clave de paginación.
        """
        pass
