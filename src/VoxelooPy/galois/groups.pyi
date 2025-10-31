from typing import Generic, TypeVar, Tuple, Union, List, Any

class CombinedMesh:
    blocks: Any
    florae: Any
    glass: Any

Index = Any

class Mesh:
    texture: Texture
    def vertex_data(self) -> memoryview: ...
    def index_data(self) -> memoryview: ...

Tensor = Any

class Texture:
    def shape(self) -> Tuple[int, int]: ...
    @property
    def data(self) -> np.ndarray: ...
    @staticmethod
    def fromarray(array: np.ndarray) -> "Texture": ...

class Vertex:
    pos: Tuple[float, float, float]
    normal: Tuple[float, float, float]
    uv: Tuple[float, float]

def to_index(arg0: Any) -> Any: ...
def to_tensor(arg0: Any) -> Any: ...
def to_mesh(arg0: Any) -> Mesh: ...
def to_wireframe_mesh(arg0: Any) -> Tensor: ...
