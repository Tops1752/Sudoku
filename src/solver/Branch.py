'''
Created on May 8, 2015

@author: bzou
'''

import copy

import logging

logging.basicConfig()
logger = logging.getLogger("Branch")
logger.setLevel(logging.DEBUG)


#===============================================================================
# get the branch of the grid
#===============================================================================
def branch(grid):
    
    node = getNode(grid)
    
    branch = []
    log = "%s (unsolved = %d) branches at %s to: "%(grid.id,grid.getUnsolved(),node.id)
    
    for v in node.pending:
        g = copy.deepcopy(grid)
        grid.addChild(g)
        success = g.cellMatrix[node.row-1][node.col-1].setValue(v)
        if success:
            branch.append(g)
            log += "%s (%d);"%(g.id,v)
        else:
            log += "%s (fail - %d)"%(g.id,v)
    
    logger.debug(log)    
    
    return branch
    
#===============================================================================
# get the node 
#===============================================================================
def getNode(grid):
    node = None
    num  = grid.dim + 1
    for l in grid.cellMatrix:
        for c in l:
            if c.value == 0 and len(c.pending)<num:
                node = c
                num  = len(c.pending)
    logger.debug("Get %s as node of %s : %s"%(node.id,grid.id,str(node.pending)))            
    return node