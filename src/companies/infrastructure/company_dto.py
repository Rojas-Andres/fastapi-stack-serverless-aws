from domain.entities import Company
from typing import Dict


class CompanyDTO:
    @staticmethod
    def to_dto(company: Company) -> Dict:
        return {
            "company_id": company.company_id,
            "name": company.name,
            "address": company.address,
        }

    @staticmethod
    def from_dto(data: Dict) -> Company:
        return Company(
            company_id=data["company_id"],
            name=data["name"],
            address=data.get("address"),
        )
