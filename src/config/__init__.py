from .logger import loggerConfig
from .default import defaultConfig

from src.utils.cliParser import cliParser
from src.utils.general import getSettings

settings = getSettings(environment=cliParser.getEnvironment(), defaultConfig=defaultConfig)
