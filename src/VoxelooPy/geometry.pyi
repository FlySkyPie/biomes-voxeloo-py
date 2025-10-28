from typing import Tuple, TypeVar, Generic

T = TypeVar('T', int, float, bool)

class Vec2(Generic[T]):
    x: T
    y: T
    def __init__(self, x: T, y: T) -> None: ...
    def tuple(self) -> Tuple[T, T]: ...

class Vec3(Generic[T]):
    x: T
    y: T
    z: T
    def __init__(self, x: T, y: T, z: T) -> None: ...
    def tuple(self) -> Tuple[T, T, T]: ...

class Vec4(Generic[T]):
    x: T
    y: T
    z: T
    w: T
    def __init__(self, x: T, y: T, z: T, w: T) -> None: ...
    def tuple(self) -> Tuple[T, T, T, T]: ...

Vec2u = Vec2[unsigned int]
Vec3u = Vec3[unsigned int]
Vec4u = Vec4[unsigned int]

Vec2i = Vec2[int]
Vec3i = Vec3[int]
Vec4i = Vec4[int]

Vec2b = Vec2[bool]
Vec3b = Vec3[bool]
Vec4b = Vec4[bool]

Vec2f = Vec2[float]
Vec3f = Vec3[float]
Vec4f = Vec4[float]

Vec2d = Vec2[double]
Vec3d = Vec3[double]
Vec4d = Vec4[double]