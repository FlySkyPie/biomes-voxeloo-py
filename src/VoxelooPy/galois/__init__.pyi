from typing import Generic, TypeVar, Tuple, Union, List, Any
import numpy as np

from . import blocks
from . import csg
from . import florae
from . import groups
from . import lighting
from . import material_properties
from . import sbo

T = TypeVar("T", bool, int, float)
RGBA = Tuple[int, int, int, int]

class Transform:
    permute: np.ndarray
    reflect: np.ndarray
    shift: np.ndarray

class Buffer:
    rank: int
    data: Any

class StorageBuffer:
    def shape(self) -> Tuple[int, int, int]: ...
    data: Any
    def view(self) -> memoryview: ...

class Level:
    MACRO: int
    MICRO: int

# Module functions
def apply(tensor: Any, transform: Transform) -> Any: ...
def shift(transform: Transform) -> Transform: ...
def permute(transform: Transform) -> Transform: ...
def reflect(transform: Transform) -> Transform: ...
def compose(t1: Transform, t2: Transform) -> Transform: ...
def to_surface(tensor: Any) -> Any: ...


__all__ = [
    "blocks",
    "csg",
    "florae",
    "groups",
    "lighting",
    "material_properties",
    "sbo",
]
