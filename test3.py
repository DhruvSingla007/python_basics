def solution(s):
    # Your code here
    ans = 0
    sol = 0
    for i in range(len(s)):
        if s[i] == '>':
            sol = sol + 1
            continue
        if s[i] == '<':
            sol = sol + ans
            continue
    
    return sol*2

s= input()

print(solution(s))