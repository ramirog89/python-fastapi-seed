from os import sys, path
from importlib import import_module


def getSettings(environment: str, defaultConfig: dict):
    '''
        getSettings function import the environment config given by argument
        when our application is run.
        @environment: string
        @defaultConfig: dictionary contains application settings
        @return: config dictionary
    '''
    try:
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))) + '/config/env')
        module = import_module(environment)
        return module.config
    except:
        return defaultConfig
