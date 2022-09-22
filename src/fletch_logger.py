import logging
import os
from datetime import datetime

class logger(object):
    def __init__(self):
        log_date = datetime.now().strftime("%Y%m%d_%H%M%S")
        format_string = '%(asctime)s %(levelname)s:%(message)s'
        # log_file = os.path.join(os.getcwd(),fname+log_date+'.log')
        log_file = "field_recommendations_"+log_date+'.log'
        logging.basicConfig(filename=log_file, level=logging.INFO, format=format_string, datefmt='%Y-%m-%d %H:%M:%S')
        logger = logging.getLogger()
        self.logger = logger

    def log_it(self, message):
        print(message)
        self.logger.info(message)