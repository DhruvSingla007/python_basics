from queue import Queue 
from random import randrange

def isSafe(r,c):
    if r > 7 or r < 0 or c < 0 or c >7:
        return False
    
    return True

def solution(src, dest):
    #Your code here
    if src == dest:
        return 0
    
    L = Queue(maxsize = 1000)
    visited = []
    
    for i in range(0,64,1):
        visited.append(False)
        
    ans = 0
    L.put(src)
    visited[src] = True

    destR = dest//8
    destC = dest%8
    
    while(not L.empty()):

        ans = ans + 1
        size = L.qsize()
        while (size > 0):
            size = size - 1
            front = L.get()
            if front == dest:
                return ans

            (r,c) = (front//8, front%8)
            reachables = []
            reachables.append((r-1, c+2))
            reachables.append((r+1, c+2))
            reachables.append((r+2, c+1))
            reachables.append((r+2, c-1))
            reachables.append((r+1, c-2))
            reachables.append((r-1, c-2))
            reachables.append((r-2, c+1))
            reachables.append((r-2, c-1))

            if (destR,destC) in reachables:
                return ans
        
            for (a,b) in reachables:
                if(isSafe(a,b) and not visited[(a*8) + b]):
                    visited[(a*8) + b] = True
                    L.put((a*8) + b)
    
    return ans



# Python3 code to find minimum steps to reach 
# to specific cell in minimum moves by Knight 
class cell: 
	
	def __init__(self, x = 0, y = 0, dist = 0): 
		self.x = x 
		self.y = y 
		self.dist = dist 
		
# checks whether given position is 
# inside the board 
def isInside(x, y, N): 
	if (x >= 1 and x <= N and
		y >= 1 and y <= N): 
		return True
	return False
	
# Method returns minimum step to reach 
# target position 
def minStepToReachTarget(knightpos, 
						targetpos, N): 
	
	#all possible movments for the knight 
	dx = [2, 2, -2, -2, 1, 1, -1, -1] 
	dy = [1, -1, 1, -1, 2, -2, 2, -2] 
	
	queue = [] 
	
	# push starting position of knight 
	# with 0 distance 
	queue.append(cell(knightpos[0], knightpos[1], 0)) 
	
	# make all cell unvisited 
	visited = [[False for i in range(N + 1)] 
					for j in range(N + 1)] 
	
	# visit starting state 
	visited[knightpos[0]][knightpos[1]] = True
	
	# loop untill we have one element in queue 
	while(len(queue) > 0): 
		
		t = queue[0] 
		queue.pop(0) 
		
		# if current cell is equal to target 
		# cell, return its distance 
		if(t.x == targetpos[0] and
		t.y == targetpos[1]): 
			return t.dist 
			
		# iterate for all reachable states 
		for i in range(8): 
			
			x = t.x + dx[i] 
			y = t.y + dy[i] 
			
			if(isInside(x, y, N) and not visited[x][y]): 
				visited[x][y] = True
				queue.append(cell(x, y, t.dist + 1)) 

# Driver Code


N = 8

	
# This code is contributed by 
# Kaustav kumar Chanda 


success = True


for i in range(100000):
    s = randrange(64)
    d = randrange(64)
    knightpos = [(s//8) + 1, (s%8) + 1] 
    targetpos = [(d//8) + 1, (d%8) + 1]
    ans = solution(s,d)
    ans2 = minStepToReachTarget(knightpos, targetpos, N)

    print(ans,ans2)
    if ans != ans2:
        success = False
        print(s,d)
        break

print(success)

