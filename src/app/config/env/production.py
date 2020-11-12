from src.app.config.default import defaultConfig

config = {
  **defaultConfig,
  'ENVIRONMENT': 'production',
  'SERVER': {
    'HOSTNAME': '127.0.0.1',
    'PORT': 7000,
    'DEBUG': False,
    'RELOAD': False,
    'LOG_LEVEL': 'info'
  },
  'SWAGGER': {
    'DOCS_URL': None,
    'REDOC_URL': None,
  }
}
