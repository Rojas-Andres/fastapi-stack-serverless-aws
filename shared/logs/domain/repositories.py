from abc import ABC, abstractmethod
from shared.logs.domain.entities import Log


class LogRepository(ABC):
    @abstractmethod
    def save_log(self, log: Log) -> None:
        pass
