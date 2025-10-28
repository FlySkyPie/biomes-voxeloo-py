from typing import Generic, TypeVar, Tuple, Union
from .blocks import BlockList, VolumeBlock, SparseBlock
import numpy as np

T = TypeVar('T', bool, int, float)
RGBA = Tuple[int, int, int, int]

from .core import bind