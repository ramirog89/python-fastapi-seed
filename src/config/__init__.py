from os import sys, path
from importlib import import_module

from .logger import loggerConfig
from .default import defaultConfig

def getSettings():
  if '--env=' in sys.argv[1]:
    sys.path.append(path.abspath('src/config/env'))
    envParam = sys.argv[1]
    environment = envParam.split('=')[1]
    try:
      module = import_module(environment)
      return module.config
    except:
      return defaultConfig
  return defaultConfig

settings = getSettings()
