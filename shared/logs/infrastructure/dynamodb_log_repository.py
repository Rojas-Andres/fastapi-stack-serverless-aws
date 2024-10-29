from shared.infrastructure.dynamodb_repository import DynamoDBRepository
from shared.logs.domain.entities import Log
from shared.logs.domain.repositories import LogRepository


class DynamoDBLogRepository(DynamoDBRepository, LogRepository):
    def save_log(self, log: Log) -> None:
        item = {
            "api": log.api,
            "timestamp": log.timestamp,
            "status_code": log.status_code,
            "response_body": log.response_body,
            "request_body": log.request_body,
            "params": log.params,
            "url": log.url,
        }
        self.put_item(item)
