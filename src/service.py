import copy
import uuid
from typing import List, Dict

from src.aws_utils import aws_put_file, aws_dump_json, aws_get_part_file_data
from src.config import conf
from src.utils import get_file_size, get_part_file_data


class KeyValueData:

    def __init__(self, s3):
        self.s3 = s3
        self.local_data_map = {
            'file_key': 'local_storage',
            'map': {}
        }
        self.data_maps: List[Dict] = [
            {
                'file_key': '',
                'map': {}
            }

        ]

    def get_data_map(self, key):
        for i in self.data_maps:
            if i['map'].get(key):
                return i

    async def get_item(self, key):
        if self.local_data_map['map'].get(key):
            return get_part_file_data('local_storage', *self.local_data_map['map'].get(key))

        data_map = self.get_data_map(key)
        if data_map:
            return await aws_get_part_file_data(self.s3, data_map['file_key'], *data_map['map'][key])

    def clear_local_storage(self):
        open('local_storage', mode='w').close()
        self.local_data_map['map'] = {}

    async def __aws_dump_local_storage(self):
        file_name = str(uuid.uuid4)
        await aws_put_file(self.s3, 'local_storage', file_name)
        await aws_dump_json(self.s3, file_name + '_map.json', self.local_data_map)
        self.data_maps.append(copy.deepcopy(self.local_data_map))
        self.clear_local_storage()

    async def set_item(self, key, value):
        file_size = get_file_size('local_storage')

        if file_size > conf['MAX_LOCAL_STORAGE_SIZE']:
            await self.__aws_dump_local_storage()

        with open('local_storage', mode='ab') as f:
            f.write(bytes(value, encoding='utf-8'))

        byte_data_range = (file_size, get_file_size('local_storage'))

        self.local_data_map['map'][key] = byte_data_range
        print(self.local_data_map['map'][key])
