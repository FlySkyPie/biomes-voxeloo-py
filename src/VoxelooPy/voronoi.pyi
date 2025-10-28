from typing import Tuple
import numpy as np
import numpy.typing as npt

def rasterize_2d(
    points: npt.NDArray[np.float32],
    shape: Tuple[int, int]
) -> npt.NDArray[np.uint32]: ...

def rasterize_3d(
    points: npt.NDArray[np.float32],
    shape: Tuple[int, int, int]
) -> npt.NDArray[np.uint32]: ...