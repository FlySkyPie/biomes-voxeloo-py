from typing import Tuple
from ctypes import c_uint8, c_int32, c_float, c_double

class Vec2b:
    x: bool
    y: bool
    def __init__(self, x: bool, y: bool) -> None: ...
    def tuple(self) -> Tuple[bool, bool]: ...

class Vec2d:
    x: c_double
    y: c_double
    def __init__(self, x: c_double, y: c_double) -> None: ...
    def tuple(self) -> Tuple[c_double, c_double]: ...

class Vec2f:
    x: c_float
    y: c_float
    def __init__(self, x: c_float, y: c_float) -> None: ...
    def tuple(self) -> Tuple[c_float, c_float]: ...

class Vec2i:
    x: c_int32
    y: c_int32
    def __init__(self, x: c_int32, y: c_int32) -> None: ...
    def tuple(self) -> Tuple[c_int32, c_int32]: ...

class Vec2u:
    x: c_uint8
    y: c_uint8
    def __init__(self, x: c_uint8, y: c_uint8) -> None: ...
    def tuple(self) -> Tuple[c_uint8, c_uint8]: ...

class Vec3b:
    x: bool
    y: bool
    z: bool
    def __init__(self, x: bool, y: bool, z: bool) -> None: ...
    def tuple(self) -> Tuple[bool, bool, bool]: ...

class Vec3d:
    x: c_double
    y: c_double
    z: c_double
    def __init__(self, x: c_double, y: c_double, z: c_double) -> None: ...
    def tuple(self) -> Tuple[c_double, c_double, c_double]: ...

class Vec3f:
    x: c_float
    y: c_float
    z: c_float
    def __init__(self, x: c_float, y: c_float, z: c_float) -> None: ...
    def tuple(self) -> Tuple[c_float, c_float, c_float]: ...

class Vec3i:
    x: c_int32
    y: c_int32
    z: c_int32
    def __init__(self, x: c_int32, y: c_int32, z: c_int32) -> None: ...
    def tuple(self) -> Tuple[c_int32, c_int32, c_int32]: ...

class Vec3u:
    x: c_uint8
    y: c_uint8
    z: c_uint8
    def __init__(self, x: c_uint8, y: c_uint8, z: c_uint8) -> None: ...
    def tuple(self) -> Tuple[c_uint8, c_uint8, c_uint8]: ...

class Vec4b:
    x: bool
    y: bool
    z: bool
    w: bool
    def __init__(self, x: bool, y: bool, z: bool, w: bool) -> None: ...
    def tuple(self) -> Tuple[bool, bool, bool, bool]: ...

class Vec4d:
    x: c_double
    y: c_double
    z: c_double
    w: c_double
    def __init__(self, x: c_double, y: c_double, z: c_double, w: c_double) -> None: ...
    def tuple(self) -> Tuple[c_double, c_double, c_double, c_double]: ...

class Vec4f:
    x: c_float
    y: c_float
    z: c_float
    w: c_float
    def __init__(self, x: c_float, y: c_float, z: c_float, w: c_float) -> None: ...
    def tuple(self) -> Tuple[c_float, c_float, c_float, c_float]: ...

class Vec4i:
    x: c_int32
    y: c_int32
    z: c_int32
    w: c_int32
    def __init__(self, x: c_int32, y: c_int32, z: c_int32, w: c_int32) -> None: ...
    def tuple(self) -> Tuple[c_int32, c_int32, c_int32, c_int32]: ...

class Vec4u:
    x: c_uint8
    y: c_uint8
    z: c_uint8
    w: c_uint8
    def __init__(self, x: c_uint8, y: c_uint8, z: c_uint8, w: c_uint8) -> None: ...
    def tuple(self) -> Tuple[c_uint8, c_uint8, c_uint8, c_uint8]: ...