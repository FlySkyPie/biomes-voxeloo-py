from typing import Generic, TypeVar, overload
from ctypes import (
    c_int8,
    c_int16,
    c_int32,
    c_int64,
    c_uint16,
    c_uint32,
    c_uint64,
    c_uint8,
)

_T = TypeVar(
    "_T",
    c_int8,
    c_int16,
    c_int32,
    c_int64,
    c_uint16,
    c_uint32,
    c_uint64,
    c_uint8,
)

class _Index(Generic[_T]):
    def __init__(self) -> None: ...
    def size(self) -> int: ...
    def get(self, pos: int) -> _T: ...
    def loads(self, blob: str) -> None: ...
    def dumps(self) -> bytes: ...
    def storage_size(self) -> int: ...

class _IndexBuilder(Generic[_T]):
    def __init__(self, pos: int, val: _T) -> None: ...
    @overload
    def add(self, span: tuple[int, int], val: _T) -> None: ...
    @overload
    def add(self, pos: int, val: _T) -> None: ...
    def build(self) -> _Index[_T]: ...

IndexBuilder_I16 = _IndexBuilder[c_int16]
IndexBuilder_I32 = _IndexBuilder[c_int32]
IndexBuilder_I64 = _IndexBuilder[c_int64]
IndexBuilder_I8 = _IndexBuilder[c_int8]
IndexBuilder_U16 = _IndexBuilder[c_uint16]
IndexBuilder_U32 = _IndexBuilder[c_uint32]
IndexBuilder_U64 = _IndexBuilder[c_uint64]
IndexBuilder_U8 = _IndexBuilder[c_uint8]

Index_I16 = _Index[c_int16]
Index_I32 = _Index[c_int32]
Index_I64 = _Index[c_int64]
Index_I8 = _Index[c_int8]
Index_U16 = _Index[c_uint16]
Index_U32 = _Index[c_uint32]
Index_U64 = _Index[c_uint64]
Index_U8 = _Index[c_uint8]

__all__ = [
    "Index_I16",
    "Index_I32",
    "Index_I64",
    "Index_I8",
    "Index_U16",
    "Index_U32",
    "Index_U64",
    "Index_U8",
    "IndexBuilder_I16",
    "IndexBuilder_I32",
    "IndexBuilder_I64",
    "IndexBuilder_I8",
    "IndexBuilder_U16",
    "IndexBuilder_U32",
    "IndexBuilder_U64",
    "IndexBuilder_U8",
]
