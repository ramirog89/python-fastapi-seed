defaultConfig = {
  'SERVER': {
    'WSGI': {
      'HOSTNAME': '127.0.0.1',
      'PORT': 5000,
      'DEBUG': True,
      'RELOAD': False,
      'LOG_LEVEL': 'debug'
    }
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
