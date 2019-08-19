# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:21:31 2019

@author: Tobias
"""

import logging
import tkinter as tk

class datamodel():
    def __init__(self):
        self.log = logging.getLogger("app.datamodel")
        self.data = {}
        self.data["id_counter"] = 0
        self.root = node(self.get_id())
        
        self.id_dict = {}
        self.id_dict[self.root.id] = self.root
        
    def get_id(self):
        i = self.data["id_counter"]
        self.data["id_counter"] += 1
        return i
    
    def init_tree(self):
        if not self.tv is None:
            self.tv.bind("<Button-3>", self.tv_rightclick)
                        
            self.iid_dict = {}
            self.tv.delete(*self.tv.get_children())
            iid = self.tv.insert("", "end", text=self.root.data["name"])
            self.iid_dict[iid] = self.root
            
            
    def make_tree(self, root=None):
        if root is None:
            pass
    
    def update_gui(self):
        if not self.tv is None:
            pass
    
    def add_node(self):
        n = node(self.get_id())
        self.id_dict[n.id] = n
        return n
        
    def tv_rightclick(self, event):
        iid = self.tv.identify_row(event.y)
        if iid:
            self.tv.selection_set(iid)
            self.context = tk.Menu(tearoff=0)
            if not self.ma is None:
                for key in self.ma:
                    self.context.add_command(label=self.ma[key]["name"], 
                                             command=
                                                 lambda 
                                                     macro=self.ma[key]["obj"], 
                                                     node=self.iid_dict[iid]: 
                                                         self.execute_macro(macro, node))
                    
            self.context.post(event.x_root, event.y_root)
        else:
            pass
        
    def execute_macro(self, macro, node):
        m = macro()
        m.execute(node)
    
class node():
    def __init__(self, a_id):
        self.defaults = {}
        self.defaults["name"] = "Node"
        self.defaults["id"] = "-1"
        
        self.data = {}
        self.setDefaults()
        
        self.id = a_id
        self.data["id"] = a_id
        self.outgoings = []
        self.log = logging.getLogger("app.datamodel.node")
    
    def add(self, a_node):
        if not node in self.outgoings:
            self.outgoings.append(a_node)
            self.log.debug("node added")
            
    def setDefaults(self):
        for key in self.defaults:
            if not key in self.data:
                self.data[key] = self.defaults[key]
            
    