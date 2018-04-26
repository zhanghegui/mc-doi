__docformat__ = 'numpydoc'

# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("numpy", "networkx", "pandas")
missing_dependencies = []

for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(dependency)

if missing_dependencies:
    raise ImportError(
        "Missing required dependencies {0}".format(missing_dependencies))
del hard_dependencies, dependency, missing_dependencies

from data.data import *
from model.adjacency import *
from model.contagion_correlation import *
from model.model import *
from model.results import *
from model.threshold import *

# module level doc-string
__doc__ = """
mcdoi - a powerfull Multi-Contagion Diffusion Of Information library for Python
=====================================================================

Main Features
-------------
- None
"""
