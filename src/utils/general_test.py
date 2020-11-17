from os import sys

from .general import getSettings
class TestModule:
  config = {}

sys.modules['test'] = TestModule
del sys.modules['test']

def test_get_imported_settings():
    imported_module = getSettings('test', {})
    assert imported_module == TestModule.config

def test_get_default_settings():
    defaultConfig = { 'server': 'localhost' }
    imported_module = getSettings('noexisting', defaultConfig)
    assert imported_module == defaultConfig

