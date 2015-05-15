'''
Created on May 8, 2015

@author: bzou
'''
import logging,Branch

logging.basicConfig()
logger = logging.getLogger("Solver")
logger.setLevel(logging.DEBUG)

#===============================================================================
# Main Solver
#===============================================================================
def solver(grid):
    
    currGrid = grid
    solution = None
    
    while solution == None:
        
        # if current grid is solved, stop
        if currGrid.getUnsolved() == 0 :
            solution = currGrid
            logger.info("Get solution for sudoku.")
            break
            
        #if not solved, branch
        branch = Branch.branch(currGrid)
        
        #if no branch is available - go back
        if len(branch) == 0:
            currGrid = getBack(currGrid)
            
        #otherwise, continue with branch
        else:
            currGrid = branch[0]   
            logger.debug("Continue with %s",currGrid.id)
            
        if currGrid == None:
            logger.warn("Failed to solve the sudoku!")
            return

    print "Solution:"
    solution.display()
    
    
#===============================================================================
# chase back to get the other branch
#===============================================================================
def getBack(grid):
    curr = grid
    parent = grid.parent
    while parent!=None:
        parent.children.remove(curr)
        #if has another branch, go for it
        if len(parent.children) > 0:
            logger.debug("Back to %s"%parent.children[0].id)
            return parent.children[0]
        else: 
            curr = parent
            parent = curr.parent
            
    return None
            
    
    