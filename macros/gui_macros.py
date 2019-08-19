# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 22:54:52 2019

@author: Tobias
"""

import basic_macro

class add_child_macro(basic_macro.basic_macro):
    name = "Knoten hinzufügen"
    
    def __init__(self):
        pass
    
    def execute(self, node):
        print("add")