import uuid

from domain.entities import Company
from domain.exceptions import CompanyNotFoundException
from infrastructure.dynamodb_company_repository import DynamoDBCompanyRepository

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
