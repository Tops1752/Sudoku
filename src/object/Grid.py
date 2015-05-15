'''
Created on May 8, 2015

@author: bzou
'''
import logging

logging.basicConfig()
logger = logging.getLogger("Cell")
logger.setLevel(logging.INFO)

from Cell import Cell

class Grid(object):
    '''
    classdocs
    '''


    def __init__(self, dim = 9, name = "Grid"):
        '''
        Constructor
        '''
        #attributes of grid
        self.id         =   name+"1"                #id of the grid
        self.dim        =   dim                     #dimension of the grid
        self.matix      =   []                      #matrix of the number
        self.cellMatrix =   self.initCellMatrix()   #matrix of the cells
        self.solved =   0                           #number of cells saved
        
        #relationship with grid in the branch
        self.parent     =   None                    #parent grid that extend self
        self.children   =   []                      #list of grids extended from self
        
        logger.info("Create grid: %s",self.id)
        
    
    
#===============================================================================
# Initial the cellMatrix and the cells
#===============================================================================
    def initCellMatrix(self):
        cellMatrix = []
        for i in range(0,self.dim):
            line    =   []
            for j in range(0,self.dim):
                cell    =   Cell(i+1,j+1,self.dim,self)
                line.append(cell)
            cellMatrix.append(line)
        return cellMatrix
    
    
#===============================================================================
# Input the value 
#===============================================================================
    def input(self,matrix):
        print "Input:"
        self.display(matrix)
        logger.debug("Input the initial values of the grid %s"%self.id)
        self.matix = matrix
        for i in range(0,self.dim):
            for j in range(0,self.dim):
                v = matrix[i][j]
                if v>0:
                    self.cellMatrix[i][j].setValue(v)
        


#===============================================================================
# Update grid when set cell value
#===============================================================================
    def updateGrid(self,cell):
        value   =   cell.value
        self.matix[cell.row-1][cell.col-1] = value
        self.solved += 1
        for l in self.cellMatrix:
            for c in l:
                #cell in the row/col/group 
                if (c.row == cell.row or c.col == cell.col or c.group == cell.group) and c.id!=cell.id:
                    #blank cell
                    if c.value == 0:
                        #remove the pending value
                        if value in c.pending:
                            c.pending.remove(value)
                    
                    else:   #fail set value because of the duplication
                        if c.value == cell.value:
                            return False
                        
                #decide if update successfully
                if c.value == 0:
                    if len(c.pending)==1:
                        logger.debug("only %d left for %s"%(c.pending[0],c.id))
                        success = c.setValue(c.pending[0])
                        if not success:
                            return False
                    elif len(c.pending)==0:  #fail set value because no available to choose
                        return False
                        
        return True
    
    
#===============================================================================
# Display the matrix
#===============================================================================]
    def display(self,m = []):
        matrix = m
        if len(m) == 0:
            matrix = self.matix
        
        print "-------------------------------"
        #Display the grid
        for i in range (0,self.dim):
            lstr = "|"
            for j in range (0,self.dim):
                if matrix[i][j] == 0:
                    lstr += " . "
                else:
                    lstr += " %d "%matrix[i][j]
                if j%3 == 2:
                    lstr += "|"
            print lstr
            if i%3 == 2:
                print "-------------------------------"
                
                
#===============================================================================
# add child
#===============================================================================
    def addChild(self,child):
        child.parent    =   self
        self.children.append(child)
        num = len(self.children)
        child.id = self.id + "-%d"%num
        
#===============================================================================
# get unmber of unsolved
#===============================================================================
    def getUnsolved(self):
        return self.dim*self.dim-self.solved