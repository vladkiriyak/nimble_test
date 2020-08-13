from pathlib import Path


def get_file_size(file_name: str):
    return Path(file_name).stat().st_size


def get_part_file_data(file_name: str, start: int, end: int):
    with open(file_name, mode='rb') as f:
        f.seek(start)
        data = f.read(end - start)

    return data
