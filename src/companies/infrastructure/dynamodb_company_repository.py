from domain.repositories import CompanyRepository
from domain.entities import Company
from shared.infrastructure.dynamodb_repository import DynamoDBRepository


class DynamoDBCompanyRepository(DynamoDBRepository, CompanyRepository):
    def save(self, company: Company) -> Company:
        item = {
            "PK": f"COMPANY#{company.company_id}",
            "SK": f"COMPANY#{company.company_id}",
            "EntityType": "Company",
            "Name": company.name,
            "Address": company.address,
        }
        self.put_item(item)
        return company

    def find_by_id(self, company_id: str) -> Company:
        item = self.get_item(f"COMPANY#{company_id}", f"COMPANY#{company_id}")
        if item:
            return Company(
                company_id=company_id, name=item["Name"], address=item.get("Address")
            )
        return None

    def update(self, company: Company) -> Company:
        self.put_item(
            {
                "PK": f"COMPANY#{company.company_id}",
                "SK": f"COMPANY#{company.company_id}",
                "EntityType": "Company",
                "Name": company.name,
                "Address": company.address,
            }
        )
        return company

    def delete(self, company_id: str) -> None:
        self.delete_item(f"COMPANY#{company_id}", f"COMPANY#{company_id}")
