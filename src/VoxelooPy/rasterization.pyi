from typing import Literal, Tuple
import numpy as np

MergeStrategy = Literal["none", "weighted", "nearest"]
BoundingBox = Tuple[Tuple[int, int, int], Tuple[int, int, int]]

def voxelize_mesh(
    vertices: np.ndarray[np.float64],
    triangles: np.ndarray[np.int32],
    scale: float,
    merge_strategy: MergeStrategy = "weighted",
    bounding_box: BoundingBox = ((0, 0, 0), (0, 0, 0))
) -> Tuple[np.ndarray[np.int32], np.ndarray[np.float64]]: ...