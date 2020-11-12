from src.app.config import defaultConfig

config = {
  **defaultConfig,
  'ENVIRONMENT': 'develop',
  'SERVER': {
    'HOSTNAME': '127.0.0.1',
    'PORT': 5000,
    'DEBUG': True,
    'RELOAD': True,
    'LOG_LEVEL': 'debug'
  }
}
