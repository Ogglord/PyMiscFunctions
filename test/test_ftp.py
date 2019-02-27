# test_ftp.py
import pytest
from futil import FtpClient,TestConfig

 
@pytest.fixture
def config():
    return TestConfig()

@pytest.fixture
def ftp(config):
    return FtpClient(config)

    
def test_session(ftp):
    result = ftp.download()
    assert result == True
    



