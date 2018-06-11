import logging


class Log:
    def __init__(self, name=None):
        self.name = name if name is not None else 'log'
        self.logger = logging.getLogger(self.name) if name is None else logging.getLogger(name)
        self.initialize()
        super().__init__()

    def initialize(self):
        self.logger.setLevel(logging.DEBUG)
        fh = self.file_handler(file='error.log')

        ch = self.console_handler()

        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # add the handlers to logger
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def file_handler(self, file=None):
        # create file handler which logs even debug messages
        if file is None:
            return False

        response = logging.FileHandler('log/' + file)
        response.setLevel(logging.DEBUG)

        return response

    def console_handler(self):
        # create console handler with a higher log level
        response = logging.StreamHandler()
        response.setLevel(logging.ERROR)

        return response

    def error(self, message=None):
        print(message)
        self.logger.error(message)

    def debug(self, message=None):
        print(message)
        self.logger.debug(message)

    def info(self, message=None):
        print(message)
        self.logger.info(message)

    def warn(self, message=None):
        self.logger.warn(message)

    def critical(self, message=None):
        self.logger.critical(message)

