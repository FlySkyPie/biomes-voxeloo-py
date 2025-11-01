from typing import Literal, Tuple, Any
from ctypes import c_uint32
import numpy as np

RGBA = c_uint32

class Box:
    v0: Tuple[int, int, int]
    v1: Tuple[int, int, int]
    def __init__(self, v0: Tuple[int, int, int], v1: Tuple[int, int, int]) -> None: ...
    def numpy(self) -> np.ndarray: ...
    def __repr__(self) -> str: ...

Dir = Literal["X_NEG", "X_POS", "Y_NEG", "Y_POS", "Z_NEG", "Z_POS"]

def voxels_to_mesh(vals: np.ndarray[Any, np.dtype[np.uint8]]) -> Any: ...
