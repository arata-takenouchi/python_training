import logging

import logtest

logging.basicConfig(level=logging.INFO)

logging.info('info')

logger = logging.getLogger(__name__)
logger.info('from main')

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logger.debug('debug')

logtest.do_something()
