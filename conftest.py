import os
import pytest

@pytest.fixture
def csv_file(tmpdir):
    with open(os.path.join(tmpdir, 'test.csv'), 'w+') as c:
        print('before test')
        yield c
        print('after test')

def pytest_addoption(parser):
    # parser.addoption('--os-name', defalut='linux', help='os name')
    parser.addoption('--os-name', help='os name')