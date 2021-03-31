#!/usr/bin/env python
# coding: utf-8
from os import listdir,system
from os.path import isfile, join
import numpy as np
class Data():
    def __init__(self):
        self.load = []
        self.load_data()
        
    def load_data(self):
        with open('case01.txt','r') as f :
            self.load.clear()
            for line in f.readlines():
                self.load.append(list(map(float,line.strip().split(','))))
            self.load = np.array(self.load)
        origin_point = self.load[0]
        
    def getData(self):
        return self.load




