from logging import getLogger
from pytest_mock import mock

from .logger import loggerService

logger = getLogger('app_debug')

def test_logger_error():
  with mock.patch.object(logger, 'error') as mock_error:
    loggerService.error('my error')
    mock_error.assert_called_once_with('my error')

def test_logger_info():
  with mock.patch.object(logger, 'info') as mock_info:
    loggerService.info('my info')
    mock_info.assert_called_once_with('my info')

def test_logger_debug():
  with mock.patch.object(logger, 'debug') as mock_debug:
    loggerService.debug('my debug')
    mock_debug.assert_called_once_with('my debug')

def test_logger_warning():
  with mock.patch.object(logger, 'warning') as mock_warning:
    loggerService.warning('my warning')
    mock_warning.assert_called_once_with('my warning')
