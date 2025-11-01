from typing import Generic, TypeVar, Tuple
import numpy as np
import numpy.typing as npt
from ctypes import (
    c_uint8,
    c_uint16,
    c_uint32,
    c_uint64,
    c_int8,
    c_int16,
    c_int32,
    c_int64,
)

T = TypeVar(
    "T",
    bool,
    float,
    c_uint8,
    c_uint16,
    c_uint32,
    c_uint64,
    c_int8,
    c_int16,
    c_int32,
    c_int64,
)

T_Scalar = TypeVar('T_Scalar', bound=np.generic)

class Tensor(Generic[T]):
    def __init__(self, shape: Tuple[int, int, int], fill: T = ...) -> None: ...
    def __str__(self) -> str: ...
    def fill(self, fill: T) -> None: ...
    def get(self, x: int, y: int, z: int) -> T: ...
    def assign(
        self,
        pos: npt.NDArray[np.int32],
        val: npt.NDArray[T_Scalar],
    ) -> None: ...
    def dumps(self) -> str: ...
    def loads(self, blob: str) -> None: ...
    def dump(self) -> bytes: ...
    def load(self, blob: str) -> None: ...
    def array(self) -> npt.NDArray[T_Scalar]: ...
    @staticmethod
    def fromarray(array: npt.NDArray[T_Scalar]) -> "Tensor[T]": ...

Tensor_Bool = Tensor[bool]
Tensor_I8 = Tensor[c_int8]
Tensor_I16 = Tensor[c_int16]
Tensor_I32 = Tensor[c_int32]
Tensor_I64 = Tensor[c_int64]
Tensor_U8 = Tensor[c_uint8]
Tensor_U16 = Tensor[c_uint16]
Tensor_U32 = Tensor[c_uint32]
Tensor_U64 = Tensor[c_uint64]
Tensor_F32 = Tensor[float]
Tensor_F64 = Tensor[float]
