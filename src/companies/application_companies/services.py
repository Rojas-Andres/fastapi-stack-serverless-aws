import json
import uuid
from typing import Any, Dict, List, Optional

from domain_companies.entities import Company
from domain_companies.exceptions import CompanyNotFoundException
from infrastructure_companies.dynamodb_company_repository import (
    DynamoDBCompanyRepository,
)

from shared.infrastructure.database import table


class CompanyService:
    def __init__(self):
        self.repository_company = DynamoDBCompanyRepository(table)

    def create_company(self, name: str, address: str) -> Company:
        company = Company(company_id=str(uuid.uuid4()), name=name, address=address)
        return self.repository_company.save(company)

    def get_company(self, company_id: str) -> Company:
        company = self.repository_company.find_by_id(company_id)
        if not company:
            raise CompanyNotFoundException(f"Company with ID {company_id} not found.")
        return company

    def update_company(self, company_id: str, name: str, address: str) -> Company:
        company = self.get_company(company_id)
        company.name = name
        company.address = address
        return self.repository_company.update(company)

    def delete_company(self, company_id: str) -> None:
        self.repository_company.delete(company_id)

    def get_paginated_companies(
        self, limit: int = 10, last_evaluated_key: Optional[str] = None
    ) -> Dict[str, Any]:
        if last_evaluated_key:
            last_evaluated_key = last_evaluated_key.replace("'", '"')
            last_evaluated_key = json.loads(last_evaluated_key)
        companies, new_last_evaluated_key = (
            self.repository_company.get_companies_paginated(limit, last_evaluated_key)
        )
        return {"items": companies, "last_evaluated_key": new_last_evaluated_key}
