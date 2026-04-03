"""Example project using the py-build-cmake build backend and pybind11."""

__version__ = "0.7.5"

import os

if os.getenv("PYBIND11_PROJECT_PYTHON_DEBUG"):
    from .module_d import *  # noqa: F403
else:
    from .module import *  # noqa: F403
