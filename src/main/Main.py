'''
Created on May 8, 2015

@author: bzou
'''
import Input
from object.Grid import Grid
from solver import Solver

input = Input.easy1()

grid = Grid()

grid.input(input)


Solver.solver(grid)
    