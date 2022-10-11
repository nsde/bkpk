"""
A super simple and lightweight zip- and unzip tool.
"""
__version__ = '0.2.7'

from .pack import *
from .unpack import *
from .models import *
from .helpers import *

# CLI
import colorama

colorama.init(autoreset=True)

