from typing import Any
import numpy as np

class Box:
    def __init__(self, v0: tuple[int, int, int], v1: tuple[int, int, int]) -> None: ...
    def numpy(self) -> np.ndarray: ...
    @property
    def v0(self) -> tuple[int, int, int]: ...
    @v0.setter
    def v0(self, value: tuple[int, int, int]) -> None: ...
    @property
    def v1(self) -> tuple[int, int, int]: ...
    @v1.setter
    def v1(self, value: tuple[int, int, int]) -> None: ...
    def __repr__(self) -> str: ...

class Dir:
    X_NEG: Dir
    X_POS: Dir
    Y_NEG: Dir
    Y_POS: Dir
    Z_NEG: Dir
    Z_POS: Dir
    @property
    def name(self) -> str: ...
    @property
    def value(self) -> int: ...

X_NEG: Dir
X_POS: Dir
Y_NEG: Dir
Y_POS: Dir
Z_NEG: Dir
Z_POS: Dir

def voxels_to_mesh(vals: np.ndarray[Any, Any]) -> Any: ...
