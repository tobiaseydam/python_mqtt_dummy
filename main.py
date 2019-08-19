# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:24:32 2019

@author: Tobias
"""

import tkinter as tk
from tkinter import ttk as ttk
import tkinter.scrolledtext as st
import logging
from classes.logTextHandler import TextHandler
from classes.datamodel import datamodel
from macros import macros

class app():
    def __init__(self):
        self.root = tk.Tk()
        self.logger = logging.getLogger("app")
        self.logger.setLevel(logging.DEBUG)
        self.create_widgets()
        #self.logger.info("Application started")
        self.init_tree()
    
    def create_widgets(self):
        self.treePane = tk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.treePane.pack(fill=tk.BOTH, expand=1)
        
        self.tree = ttk.Treeview(self.treePane)
        self.treePane.add(self.tree)
        
        self.infoText = st.ScrolledText(self.treePane, state='disabled')
        self.treePane.add(self.infoText)
        
        self.logPane = tk.PanedWindow(self.root, orient=tk.VERTICAL)
        self.logPane.pack(fill=tk.BOTH, expand=1)
        
        self.logText = st.ScrolledText(self.logPane, height=8, state='disabled')
        self.logPane.add(self.logText)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        logHandler = TextHandler(self.logText)
        logHandler.setFormatter(formatter)
        self.logger.addHandler(logHandler)
        
    def init_tree(self):
        self.dm = datamodel()
        self.dm.tv = self.tree
        self.dm.ma = macros
        self.dm.init_tree()
        
    def run(self):
        self.root.mainloop()



if __name__ == "__main__":
    app = app()
    app.run()