from typing import Literal, Tuple
from numpy.typing import NDArray
import numpy as np

MergeStrategy = Literal["none", "weighted", "nearest"]
BoundingBox = Tuple[Tuple[int, int, int], Tuple[int, int, int]]

def voxelize_mesh(
    vertices: NDArray[np.float64],
    triangles: NDArray[np.int32],
    scale: float,
    merge_strategy: MergeStrategy = "weighted",
    bounding_box: BoundingBox = ((0, 0, 0), (0, 0, 0)),
) -> Tuple[NDArray[np.int32], NDArray[np.float64]]: ...
