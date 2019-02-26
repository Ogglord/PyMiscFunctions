# test_fuzip.py
import pytest
from futil import Session
from futil import TestConfig
from futil import CacheForTest, CacheRedis
import uuid

@pytest.fixture
def sessionid():
    return uuid.uuid4().hex

@pytest.fixture
def config():
    return TestConfig()

@pytest.fixture
def cache(config):
    return CacheForTest(config)

@pytest.fixture
def session(config, sessionid, cache):
    return Session(config, sessionid, cache)
    
def test_session(session):
    session["name"] = "Oscar"
    assert session["name"] == "Oscar"
    



