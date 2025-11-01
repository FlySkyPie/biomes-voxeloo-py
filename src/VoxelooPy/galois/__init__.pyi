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
