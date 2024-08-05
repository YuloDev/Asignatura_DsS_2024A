import logging
from .models import Log

class DatabaseLogHandler(logging.Handler):
    def emit(self, record):
        log_entry = Log(
            level=record.levelname,
            message=record.getMessage(),
            module=record.module,
            function=record.funcName,
            line=record.lineno
        )
        log_entry.save()
