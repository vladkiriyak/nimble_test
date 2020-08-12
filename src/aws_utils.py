import json
from typing import List

from botocore.response import StreamingBody

from src.config import conf


async def aws_put_file(s3, file_name, created_file_name):
    response = await s3.upload_file(file_name, conf['BUCKET'], created_file_name)
    return response


async def aws_dump_json(s3, file_name, data: dict):
    data = json.dumps(data)
    response = await s3.put_object(Body=data, Bucket=conf['BUCKET'], Key=file_name)
    return response


async def aws_get_part_file_data(s3, name, start, end):
    r = await s3.get_object(Bucket=conf['BUCKET'], Key=name, Range=f'bytes={start}-{end}')
    stream: StreamingBody = r['Body']

    return stream.read()


async def aws_get_files(s3) -> List[str]:
    resp = await s3.list_objects(Bucket=conf['BUCKET'])
    return [file['Key'] for file in resp['Contents']]
