from pytest_mock import mock
from .general import getSettings

def test_get_settings():
    module_obj = {'name': {}, 'another_name': {}, 'config': {} }
    with mock.patch.object('importlib.import_module', module_obj) as m:
      a = getSettings('default', { '1': 2 })
      print('m' ,m)
      print('a', a)
      assert 1 == 2