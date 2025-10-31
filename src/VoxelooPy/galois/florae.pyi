from typing import Tuple, List, Any

class GeometryBuffer:
    vertices: Any
    indices: Any
    def vertex_data(self) -> memoryview: ...
    def index_data(self) -> memoryview: ...

Index = Any
IndexBuilder = Any

class QuadVertex:
    def __init__(
        self,
        pos: Tuple[float, float, float],
        normal: Tuple[float, float, float],
        uv: Tuple[float, float],
        arg3: float,
        arg4: int,
    ) -> None: ...
    def pos(self) -> Tuple[float, float, float]: ...
    def normal(self) -> Tuple[float, float, float]: ...
    def uv(self) -> Tuple[float, float]: ...
    def texture(self) -> int: ...

class Quads:
    vertices: List[QuadVertex]
    indices: List[int]

def to_geometry(tensor: Any, growth: Any, muck: Any, index: Any) -> GeometryBuffer: ...
