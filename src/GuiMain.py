#!/usr/bin/env python
# coding: utf-8
from tkinter import *
import tkinter as tk
from os import listdir,system
from os.path import isfile, join
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import math
import time
from loadData import Data
from Car import car
from Map import map
from Fuzzy import fuzzy

class gui(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.windows = master
        self.grid()
        self.create_windows()
        self.data = []
        self.edges = []

    def create_windows(self):
        self.windows.title("HW1")
        self.result_figure = Figure(figsize=(8,8), dpi=100)
        self.result_canvas = FigureCanvasTkAgg(self.result_figure, self.windows)
        self.result_canvas.draw()
        self.result_canvas.get_tk_widget().grid(row=6, column=0, columnspan=3, sticky=tk.W+tk.E)
        self.front_text = tk.Label(self.windows, text="前方:").grid(row=2,column=0, sticky=tk.W+tk.E)
        self.left_text = tk.Label(self.windows, text="左方:").grid(row=3,column=0, sticky=tk.W+tk.E)
        self.right_text = tk.Label(self.windows, text="右方:").grid(row=4,column=0, sticky=tk.W+tk.E)
        self.show = tk.Button(self.windows, text='Next', command=self.run).grid(row=1, column=0, sticky=tk.W+tk.E)
        self.show = tk.Button(self.windows, text='Show', command=self.run).grid(row=1, column=1, sticky=tk.W+tk.E)
    
    def run(self):
        d = Data()
        self.data = d.getData()
        m = map(self.data)
        self.edges = m.getEdges()
        c = car(self.data[0])
        f = fuzzy()
        Y = c.getPosition()
        while(Y[1] < 43):
            self.mapping(self.edges)
            self.draw_car(c.getPosition())
            c.sensor(self.edges)
            F, L, R = c.getDistance()
            self.front_value = tk.Label(windows, text= str(F)).grid(row=2,column=1, sticky=tk.W+tk.E)
            self.left_value = tk.Label(windows, text= str(L)).grid(row=3,column=1, sticky=tk.W+tk.E)
            self.right_value = tk.Label(windows, text= str(R)).grid(row=4,column=1, sticky=tk.W+tk.E)
            c.setWheel(f.system(F, L, R))
            c.update_car_direction()
            c.update_car_pos()
            self.result_figure.clear()
            
            
    def mapping(self, edges):
        self.result_figure.clf()
        self.draw_map(edges[0],edges[1], 'r')
        self.draw_map([-6,0], [6, 0], 'black')
        for i in range(2,len(edges) - 1):
            self.draw_map(edges[i],edges[i+1], 'b')
    
    def draw_map(self,p_1, p_2, c):
        self.result_figure.a = self.result_figure.add_subplot(111)
        min_v, max_v, ymin, ymax = self.set_maxmin(p_1, p_2)
        x = np.linspace(min_v, max_v)
        if (p_2[0] - p_1[0] == 0):
            self.result_figure.a.vlines(p_1[0], ymin, ymax, color = c)
        else:
            slope = (p_2[1] - p_1[1])/(p_2[0] - p_1[0])
            intercept = p_1[1]
            y = (slope*x) + intercept
            self.result_figure.a.plot(x, y, color = c)
        self.result_figure.a.set_title('Fuzzy System')
        self.result_canvas.draw()
        
    def set_maxmin(self, p1, p2):
        if p1[0] < p2[0]:
            x_m = p1[0]
            x_M = p2[0]
        else:
            x_m = p2[0]
            x_M = p1[0]  
        if p1[1] < p2[1]:
            y_m = p1[1]
            y_M = p2[1]
        else:
            y_m = p2[1]
            y_M = p1[1]
        return x_m, x_M, y_m, y_M
    
    def draw_car(self,point):
        self.result_figure.b = self.result_figure.add_subplot(111)
        p_x = point[0]
        p_y = point[1]
        r = 3.0
        theta = np.arange(0, 2*np.pi, 0.01)
        x = p_x + r * np.cos(theta)
        y = p_y + r * np.sin(theta)
        self.result_figure.b.plot(p_x, p_y, 'ro')
        self.result_figure.b.plot(x, y, color = 'g')
        self.result_canvas.draw()

if __name__ == "__main__":
    windows = tk.Tk()
    app = gui(windows)
    windows.mainloop()
