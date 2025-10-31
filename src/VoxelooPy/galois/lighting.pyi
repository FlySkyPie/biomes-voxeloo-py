from typing import Any

from .sbo import StorageBuffer

class Buffer:
    rank: StorageBuffer
    data: StorageBuffer

def to_buffer(tensor: Any, isomorphisms: Any) -> Buffer: ...
