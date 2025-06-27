import logging
import os

from pyexpat.errors import messages


class Logger:
    def __init__(self,
             log_file   :str        # path of the logger file
             )  -> None:
        self.level = logging.DEBUG
        self.log_file = log_file
        logs_dir = os.path.abspath('tests/logs')
        if not os.path.exists(logs_dir):
            os.makedirs(logs_dir)

        log_path = os.path.join(logs_dir, f"{self.log_file}.log")
        self.logger=logging.getLogger(self.log_file)

        if not self.logger.handlers:

            file_handler = logging.FileHandler(log_path)
            file_handler.setLevel(self.level)

            formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                                          datefmt = "%Y-%m-%d %H:%M:%S")

            file_handler.setFormatter(formatter)

            self.logger.addHandler(file_handler)
            self.logger.setLevel(self.level)

    def info(self,
             message    :str        # message for the logger file
             ) -> None:
        self.logger.info(message)

    def error(self,
             message    :str        # message for the logger file
              ) -> None:
        self.logger.error(message)

    def debug(self,
             message    :str        # message for the logger file
              ) -> None:
        self.logger.debug(message)

    def warning(self,
             message    :str        # message for the logger file
                ) -> None:
        self.logger.warning(message)