# my_package/__init__.py

from .template_loader import get_template_path  # Import template functions

# Optional: Define __all__ to specify what gets imported when using `from my_package import *`
__all__ = ["get_template_path"]