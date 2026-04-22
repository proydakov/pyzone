"""Example project using the py-build-cmake build backend and pybind11."""

import os

if os.getenv("PYBIND11_PROJECT_PYTHON_DEBUG"):
    from .module_d import *  # noqa: F403
    from .module_d import __version__
else:
    from .module import *  # noqa: F403
    from .module import __version__
