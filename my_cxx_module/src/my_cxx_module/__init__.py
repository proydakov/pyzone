"""Example project using the py-build-cmake build backend and pybind11."""

__version__ = "0.7.5"

import os
import typing

if not typing.TYPE_CHECKING and os.getenv("PYBIND11_PROJECT_PYTHON_DEBUG"):
    from .module_d import *  # noqa: F403
    from .module_d import __version__  # noqa: F401, RUF100
else:
    from .module import *  # noqa: F403
    from .module import __version__  # noqa: F401, RUF100

