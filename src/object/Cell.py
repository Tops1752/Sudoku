'''
Created on May 8, 2015

@author: bzou
'''

import logging

logging.basicConfig()
logger = logging.getLogger("Cell")
logger.setLevel(logging.INFO)

class Cell(object):
    '''
    classdocs
    '''

    def __init__(self, row=0,col=0,dim=0,grid=None):
        '''
        Constructor
        '''
        self.id     = "c%d-%d"%(row,col)    #id of the cell
        self.row    = row                   #row of the grid
        self.col    = col                   #column of the grid
        self.group  = self.getGroup()       #group of the grid
        self.value  = 0                     #value of the cell
        self.pending= range(1,dim+1)        #the potential values of the cell
        self.parent = grid                  #parent grid
        
        logger.debug("Create a cell %s"%self.id)
    
    
#===============================================================================
# define the group of the cell - called in init
#===============================================================================
    def getGroup(self):
        if self.row==0 or self.col ==0:
            return 0
        else:
            r       = (self.row-1)/3
            c       = (self.col-1)/3
            group   = r+1+c*3
            return group
        
#===============================================================================
# set value of this cell
#===============================================================================
    def setValue(self,value):
        if self.value == 0:
            #set value for this cell
            self.value  =   value
            self.pending=   []
            logger.debug("Set %d to %s - grid %s"%(value,self.id,self.parent.id))
            #update grid
            success = self.parent.updateGrid(self)
            return success
        elif self.value!=value:
            logger.error("Resetting value %d to %s, current value is %d"%(value,self.id,self.value))
            return False
        else:
            logger.debug("Reset same value to %s"%self.id)
            return True
        
#===============================================================================
# get status
#===============================================================================
    def status(self):
        return "%s: value = %d, pending = %s"%(self.id,self.value,str(self.pending))

        
if __name__ == '__main__':
    
    cell = Cell(row=1,col=2,dim=9)
    print cell.group
    print cell.id
    print cell.pending