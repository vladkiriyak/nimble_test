import os

import pytest


@pytest.fixture
def file_32_bytes():
    with open('file.txt', mode='w') as file:
        file.write("abcd" * 8)

    yield 'file.txt'
    os.remove('file.txt')
