defaultConfig = {
  'ENVIRONMENT': 'local',
  'SERVER': {
    'HOSTNAME': '127.0.0.1',
    'PORT': 5000,
    'DEBUG': True,
    'RELOAD': False,
    'LOG_LEVEL': 'debug'
  },
  'API': {
    'TITLE': 'REST API',
    'DESCRIPTION': 'Minimal rest api setup',
    'VERSION': '0.1.0',
  },
  'SWAGGER': {
    'DOCS_URL': '/docs',
    'REDOC_URL': '/redoc_docs',
  },
  'JWT': {
    'SECRET_KEY': 'some-secret-key'
  },
  'DATABASE': {
    'SQLALCHEMY': {
      'PREFIX': 'DB.',
      'CONFIG': {
        'DB.URL': 'sqlite:///./sql_app.db',
        'DB.ECHO': True
      }
    }
  },
}
