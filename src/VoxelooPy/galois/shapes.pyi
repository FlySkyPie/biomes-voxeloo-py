from typing import Tuple, Any

class Box:
    def pos(self) -> Tuple[int, int, int]: ...
    len: int

Boxes = Any

BoxesBuilder = Any

class Edge:
    def v0(self) -> Tuple[float, float, float]: ...
    def v1(self) -> Tuple[float, float, float]: ...

GeometryBuffer = Any

Index = Any

IndexBuilder = Any

Level = Any

MACRO = Any

MICRO = Any

class Quad:
    def pos(self) -> Tuple[int, int, int]: ...
    lvl: Level

Quads = Any

QuadsBuilder = Any

class WireframeMesh:
    def vertex_data(self) -> memoryview: ...
    def index_data(self) -> memoryview: ...

WireframeMeshBuilder = Any

def to_geometry(tensor: Any) -> GeometryBuffer: ...
def to_glass_occlusion_tensor() -> Any: ...
def to_isomorphism_id() -> Any: ...
def to_occlusion_tensor() -> Any: ...
def to_tensor() -> Any: ...
