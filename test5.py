import math
def solution(n):
    # Your code here
    x = math.log(n,2)
    
    if x == math.floor(x):
        return x
     
    y = math.floor(x)
    extra = min(abs(pow(2,y) - n), pow(2,y+1) - n)
    
    return y + extra

print(solution(356365465435343551351351354354543531513513543543433513513154364354))