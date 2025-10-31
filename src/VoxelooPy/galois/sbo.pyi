from typing import  Tuple, List
from ctypes import c_uint32

class StorageBuffer:
    def shape(self) -> Tuple[int, int, int]: ...
    data: List[c_uint32]
    def view(self) -> memoryview: ...

class Buffer:
    rank: StorageBuffer
    data: StorageBuffer
