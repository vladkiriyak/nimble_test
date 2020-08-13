def get_node_ip(key: str) -> int:
    ...


async def get_value_from_node(node_ip: int, key: str) -> bytes:
    ...


async def put_value_in_node(node_ip: int, key: str, value: bytes) -> None:
    ...
