
import logging
from datetime import datetime
from pytz import timezone
import pathlib

from cvxport import Config
from cvxport import utils


class Logger:
    # TODO: if create more than 2 workers in the same script, logging of the 2nd worker will contaminate the 1st one
    def __init__(self, name: str):
        self.name = name.replace(':', '')

        # set up directory
        today = datetime.strftime(datetime.now(timezone('EST')), '%Y-%m-%d')
        path = pathlib.Path(Config['log_path']) / today
        filename = utils.get_next_filename(pathname=path, file_prefix=self.name)

        # get logger and formatter
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(Config['log_level'])
        formatter = logging.Formatter(fmt=Config['log_format'], datefmt=Config['log_date_format'])

        # set up stream handler
        handler = logging.StreamHandler()
        handler.setLevel(Config['log_level'])
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # configure log output
        self.logger.info(f'Log file: {filename}')
        handler = logging.FileHandler(filename=filename)
        handler.setLevel(Config['log_level'])
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def debug(self, msg):
        self.logger.debug(msg)

    def info(self, msg):
        self.logger.info(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def exception(self, msg):
        self.logger.exception(msg)
