# from typing import Dict, List
# from pathlib import Path
#
# data_maps: List[Dict] = [
#     {
#         'file_key': 'local',
#         'map': {}
#     }
#
# ]
#
# with open('test_aws_file.txt', mode='r') as f:
#     print(f.seek(0))
#     print(f.read(1))
#     print(f.tell())
# #
#
# # print(Path('test_aws_file.txt').stat().st_size)

import hashlib
print(int(hashlib.md5(b'dasd').digest()))