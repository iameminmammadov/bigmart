import logging
import sys
from datacube_bigmart import config


LOGGING_MSG_FORMAT = "%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s"
LOGGING_DATE_FORMAT = '%d-%b-%y %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=LOGGING_MSG_FORMAT, datefmt=LOGGING_DATE_FORMAT)
logger = logging.getLogger(__name__)
c_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(c_handler)
