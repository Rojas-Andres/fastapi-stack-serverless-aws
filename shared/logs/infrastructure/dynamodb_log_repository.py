from logs.domain.repositories import LogRepository
from logs.domain.entities import Log
from shared.infrastructure.dynamodb_repository import DynamoDBRepository


class DynamoDBLogRepository(DynamoDBRepository, LogRepository):
    def save_log(self, log: Log) -> None:
        item = {
            "PK": f"API#{log.api}",
            "SK": log.timestamp,
            "StatusCode": log.status_code,
            "ResponseBody": log.response_body,
            "RequestBody": log.request_body,
            "Params": log.params,
            "URL": log.url,
        }
        self.put_item(item)
