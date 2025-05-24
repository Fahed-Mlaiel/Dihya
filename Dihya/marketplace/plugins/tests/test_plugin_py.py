import pytest
from importlib import import_module

plugin = import_module('..plugin', __package__)

def test_plugin_run():
    context = type('Context', (), {'log': lambda *a, **kw: None})()
    res = plugin.run({'lang': 'fr'}, context)
    assert res['success'] is True
    assert isinstance(res['message'], str)

def test_plugin_languages():
    for lang in ['fr', 'en', 'ar', 'tzr']:
        res = plugin.run({'lang': lang}, None)
        assert res['success'] is True
