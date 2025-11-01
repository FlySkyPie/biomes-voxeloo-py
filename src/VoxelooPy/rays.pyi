from typing import List, Tuple
from ctypes import c_float
import numpy as np

from .geometry import Vec2i, Vec3f
from .spatial import DensityMap, ColorMap

def integrate(
    dm: DensityMap, src: Vec3f, dir: Vec3f, max_distance: float = 100.0
) -> float: ...
def integrate_approx(
    dm: DensityMap, src: Vec3f, dir: Vec3f, max_distance: float = 100.0
) -> float: ...
def render_orthographic(
    dm: DensityMap,
    size: Vec2i,
    src: Vec3f,
    dir: Vec3f,
    up: Vec3f = Vec3f(c_float(0.0), c_float(-1.0), c_float(0.0)),
    far: float = 100.0,
) -> np.ndarray: ...
def render_orthographic_color(
    cm: ColorMap,
    normals: np.ndarray,
    size: Vec2i,
    src: Vec3f,
    dir: Vec3f,
    lighting_dir: Vec3f,
    up: Vec3f = Vec3f(c_float(0.0), c_float(-1.0), c_float(0.0)),
    far: float = 100.0,
    zoom: float = 1.0,
    distance_capacity: float = 0.5,
) -> np.ndarray: ...
def render_orthographic_approx(
    dm: DensityMap,
    size: Vec2i,
    src: Vec3f,
    dir: Vec3f,
    up: Vec3f = Vec3f(c_float(0.0), c_float(-1.0), c_float(0.0)),
    far: float = 100.0,
) -> np.ndarray: ...
def render_camera_sequence(
    dm: DensityMap,
    cameras: List[Tuple[float, float, float, float, float, float]],
    size: Vec2i,
    up: Vec3f = Vec3f(c_float(0.0), c_float(-1.0), c_float(0.0)),
    far: float = 100.0,
) -> np.ndarray: ...
