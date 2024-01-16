import logging


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# pylint: skip-file
#pylint is triggerin odd errors espicaly realted to the
# string interpolation which is function as expected so i have disabled it for this file
class LoggableObject():
    def initialize(self, verbose):
        if verbose:
            logging.getLogger().setLevel(logging.DEBUG)

    def get_logger(self):
        return logging.getLogger()

    def log_info(self, key, message):
        logger = logging.getLogger()
        logger.info("{} - {}".format(key, message))

    def log_error(self, key, message):
        logger = logging.getLogger()
        logger.error("{} - {}".format(key, message))

    def log_warn(self, key, message):
        logger = logging.getLogger()
        logger.warning("{} - {}".format(key, message))

    def log_debug(self, key, message):
        logger = logging.getLogger()
        logger.debug("{} - {}".format(key, message))

    def log_critical(self, key, message):
        logger = logging.getLogger()
        logger.critical("{} - {}".format(key, message))
