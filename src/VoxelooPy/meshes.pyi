from typing import Any
import numpy as np
import numpy.typing as npt

class Mesh:
    vertices: npt.NDArray[np.float32]
    triangles: npt.NDArray[np.int32]
    
    def __init__(self) -> None: ...
    @staticmethod
    def loads(bytes: str) -> 'Mesh': ...
    def dumps(self) -> str: ...
    def to_blocks(self, quantization: float = 1.0) -> Any: ...  # Returns BlockList[RGBA]