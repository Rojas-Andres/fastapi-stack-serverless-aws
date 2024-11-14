from domain_companies.entities import Company
from domain_companies.repositories import CompanyRepository
from typing import List, Tuple, Optional
from boto3.dynamodb.conditions import Attr, Key
from shared.infrastructure.dynamodb_repository import DynamoDBRepository
import json


class DynamoDBCompanyRepository(DynamoDBRepository, CompanyRepository):
    def save(self, company: Company) -> Company:
        item = {
            "PK": f"COMPANY",
            "SK": f"{company.company_id}",
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

    def get_companies_paginated(
        self, limit: int, last_evaluated_key: Optional[dict] = None
    ) -> Tuple[List[Company], Optional[dict]]:
        query_kwargs = {
            "KeyConditionExpression": Key("PK").eq("COMPANY"),
            "Limit": limit,
        }
        if last_evaluated_key:
            query_kwargs["ExclusiveStartKey"] = last_evaluated_key

        response = self.table.query(**query_kwargs)
        items = [
            Company(
                company_id=item["SK"], name=item["Name"], address=item.get("Address")
            )
            for item in response.get("Items", [])
        ]
        last_evaluated_key = response.get("LastEvaluatedKey")

        return items, last_evaluated_key
