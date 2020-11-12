loggerConfig = {
  "version": 1,
  "disable_existing_loggers": False,
  "formatters": {
    "simple": {
      "format": "[%(asctime)s] %(levelname)s: %(message)s"
    },
    "complex": {
      "format": "%(asctime)s - %(name)s - %(levelname)s - %(process)s - %(message)s"
    }
  },
  "handlers": {
    "console": {
      "class": "logging.StreamHandler",
      "level": "DEBUG",
      "formatter": "complex",
      "stream": "ext://sys.stdout"
    },
    "info_file_handler": {
      "class": "logging.handlers.RotatingFileHandler",
      "level": "INFO",
      "formatter": "simple",
      "filename": "./logs/info.log",
      "encoding": "utf8"
    },

    "error_file_handler": {
      "class": "logging.handlers.RotatingFileHandler",
      "level": "ERROR",
      "formatter": "complex",
      "filename": "./logs/errors.log",
      "maxBytes": 10485760,
      "backupCount": 20,
      "encoding": "utf8"
    }
  },
  "loggers": {
    "app_debug": {
      "level": "DEBUG",
      "handlers": ["console", "info_file_handler", "error_file_handler"],
      "propagate": False
    },
    "app_production": {
      "level": "WARNING",
      "handlers": ["console", "info_file_handler"],
      "propagate": False
    }
  }
}