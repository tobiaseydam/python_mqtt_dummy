# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 21:51:56 2019

@author: Tobias
"""

class basic_macro:
    export = True
    name = "basic macro"
    types = [{"name":"node", "subtypes":True}]
        
    def __init__(self):
        pass

    def execute(self, node):
        print(node.data["name"])

    
    