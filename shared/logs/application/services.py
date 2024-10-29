from logs.domain.repositories import LogRepository
from logs.domain.entities import Log
from datetime import datetime


class LogService:
    def __init__(self, repository: LogRepository):
        self.repository = repository

    def log_response(
        self,
        api: str,
        status_code: int,
        response_body: dict,
        request_body: dict = None,
        params: dict = None,
        url: str = None,
    ):
        log = Log(
            api=api,
            timestamp=datetime.utcnow().isoformat(),
            status_code=status_code,
            response_body=response_body,
            request_body=request_body,
            params=params,
            url=url,
        )
        self.repository.save_log(log)
