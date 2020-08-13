import time

from node.src.utils import get_file_size, get_part_file_data


class TestMain:
    def test_get_file_size(self, file_32_bytes):
        assert get_file_size(file_32_bytes) == 32

    def test_get_part_file_data(self, file_32_bytes):
        assert get_part_file_data(file_32_bytes, 2, 6) == b'cdab'
