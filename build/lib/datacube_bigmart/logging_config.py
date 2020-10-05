import logging
import sys


#def logging_configuration():
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.setLevel(logging.INFO)
c_handler = logging.StreamHandler() #sys.stdout
c_handler.setLevel(logging.INFO)

c_format = logging.Formatter("%(asctime)s — %(name)s — %(levelname)s —" "%(funcName)s:%(lineno)d — %(message)s")
c_handler.setFormatter(c_format)

logger.addHandler(c_handler)
logger.warning('This is a warning')
logger.error('This is an error')
logging.info('This is an information')

#logging.getLogger().setLevel(logging.INFO)
#system_handler.setFormatter(format_logging)
#logger.addHandler(system_handler)
#    return logger

#import logging

#logging.basicConfig(level=logging.INFO)
#logging.info('This will get logged')


'''
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning('This is a warning')
logger.error('This is an error')

'''

