import logging

logger = logging.getLogger(__name__)

logger.error('api call is failed')

logger.error({
    'action': 'create',
    'status' : 'fail',
    'message': 'api call is failed'
})

logger.info({
    'action': 'save',
    'csv_file': self.csv_file,
    'force': True,
    'status': 'run'
})