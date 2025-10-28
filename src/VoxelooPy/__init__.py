from __future__ import annotations

from typing import TYPE_CHECKING

from .voxeloo import __doc__, __version__, shards

if TYPE_CHECKING:
    from . import biomes  # noqa: F401
    from ._biomes import (
        VolumeBlock,
        SparseBlock,
        BlockList,
    )

__all__ = [
    "__doc__",
    "__version__",
    "shards",
    "VolumeBlock",
    "SparseBlock",
    "BlockList",
]
