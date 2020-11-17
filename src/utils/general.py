from os import sys, path
from importlib import import_module


def getSettings(environment: str, defaultConfig: dict):
    try:
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))) + '/config/env')
        module = import_module(environment)
        return module.config
    except:
        return defaultConfig
