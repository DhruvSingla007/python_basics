def solution(x, y):
    # Your code here
    
    if x == y and x != "1":
        return "impossible"
     
    ans = 0
     
    mBomb = int(x) #1
    fBomb = int(y) #3
     
    while(mBomb > 1 and fBomb > 1):
        if mBomb > fBomb:
            ans = ans + (mBomb//fBomb)
            mBomb = mBomb - (fBomb*(mBomb//fBomb))
        else :
            ans  = ans + (fBomb//mBomb)
            fBomb = fBomb - (mBomb*(fBomb//mBomb))

         
    
    if not(mBomb == 1 or fBomb == 1):
        return "impossible"
    
    return ans + max(mBomb,fBomb) - min(mBomb,fBomb)

ans = solution("7","7")
print(ans)