from .utils import MetaSingle
from enum import Enum


class LevelEnum(Enum):
    info = 'INFO'
    critical = 'CRITICAL'
    error = 'ERROR'
    warning = 'WARNING'


class Logging(metaclass=MetaSingle):
    def __init__(self, file_name: str) -> None:
        self.file_name: str = file_name

    def _write_log(self, level: LevelEnum, msg: str) -> None:
        """Write to log file

        Args:
            level (str): level of log severity
            msg (str): log message
        """

        with open(self.file_name, 'a') as log_file:
            log_file.write(f'[{level.name}] - {msg}\n')

    def info(self, msg: str):
        self._write_log(LevelEnum.info, msg)

    def critical(self, msg: str):
        self._write_log(LevelEnum.critical, msg)

    def error(self, msg: str):
        self._write_log(LevelEnum.error, msg)

    def warning(self, msg: str):
        self._write_log(LevelEnum.warning, msg)
