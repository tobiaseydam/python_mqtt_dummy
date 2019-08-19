# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:50:56 2019

@author: Tobias
"""

import inspect
import sys
from os.path import dirname, basename, isfile, join
import glob

modules = glob.glob(join(dirname(__file__), "*.py"))
__all__ = [ basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]


macros = {}

for name, obj in inspect.getmembers(sys.modules["__main__"], inspect.isclass):
    if hasattr(obj, "export"):
        macros[name] = {"name":obj.name, "obj":obj, "types":obj.types}
            
print(macros)