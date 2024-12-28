
def remove(chain): # [3,1,1,1,7]
   
  for i in range(len(chain)):
    tempChain = chain.remove(i)
    if trySplit(tempChain):
        return True
    
      
    
def trySplit(chain):
     
     for i in range(len(chain)):
       if sum(chain[:i+1]) == sum(chain[i:]): # compare sum of left and right gold
          return True 
       return False

def Main():
  print(remove([3,1,1,1,7]))


Main()