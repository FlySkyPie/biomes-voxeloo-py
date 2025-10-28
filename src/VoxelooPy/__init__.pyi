from typing import Generic, TypeVar, Tuple, Union
from .blocks import BlockList, VolumeBlock, SparseBlock
from .culling import AABB, OcclusionBuffer, OcclusionCuller
from .shards import shard_encode, shard_decode
from .spatial import DensityMap, ColorMap
from .voronoi import rasterize_2d, rasterize_3d
from .galois import (
    Transform, MaterialBuffer, CheckboardPosition, MoistureLevel,
    Samples, Sampler, Index, IndexBuilder, QuadVertex, Quads,
    GeometryBuffer, Vertex, Texture, CombinedMesh, Buffer,
    StorageBuffer, Level, Quad, Box, Edge, WireframeMesh
)
from .meshes import Mesh
from .geometry import (
    Vec2, Vec3, Vec4,
    Vec2u, Vec3u, Vec4u,
    Vec2i, Vec3i, Vec4i,
    Vec2b, Vec3b, Vec4b,
    Vec2f, Vec3f, Vec4f,
    Vec2d, Vec3d, Vec4d
)
from .noise import SimplexNoise, noise
from .primitives import Node, xy, xyz
from .rasterization import voxelize_mesh
from .rays import (
    integrate,
    integrate_approx,
    render_orthographic,
    render_orthographic_color,
    render_orthographic_approx,
    render_camera_sequence
)
from .tensors import (
    Tensor, Tensor_Bool,
    Tensor_I8, Tensor_I16, Tensor_I32, Tensor_I64,
    Tensor_U8, Tensor_U16, Tensor_U32, Tensor_U64,
    Tensor_F32, Tensor_F64
)
import numpy as np

T = TypeVar('T', bool, int, float)
RGBA = Tuple[int, int, int, int]  # Used by spatial.ColorMap

from .core import bind
from .runs import Index, IndexBuilder