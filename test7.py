def solution(s):
  s1 = ''
  s2 = ''

  p1 = 0
  p2 = len(s) - 1

  smallestString = ''

  while(p1 < p2):

    s1 = s1 + s[p1]
    s2 = s[p2] + s2

    if p1 == p2- 1 and s1 == s2:
      if smallestString == '':
          return (len(s)//len(s1))
      print('Reached 1')
      return (len(s)//len(s1)) * (len(s1)//len(smallestString))

    remaining_s_len = p2 - p1 - 1

    if s1 == s2 and remaining_s_len < len(s1) and remaining_s_len != 0:
      print('reached 2')
      return 1
    
    if s1 == s2 and remaining_s_len == len(s1) and s[p1 + 1: p2] == s1:
      print('reached 3')
      if smallestString == '':
          return (len(s)//len(s1))
      return (len(s)//len(s1)) * (len(s1)//len(smallestString))
    
    if s1 == s2 and remaining_s_len % len(s1) == 0 and len(smallestString) < len(s1):
      print('reached 4')
      smallestString = s1
      print(smallestString)
    
    p1 = p1 + 1
    p2 = p2 - 1
  
  return 1
      
testCase1 = "abcabcabc"
testCase2 = "abbc"
testCase3 = "abba"
testCase4 = "abcabcabcabc"
testCase5 = "abcabcacbabc"
testCase6 = "abcabcdabc"
testCase7 = "abcaabcaabca"

'''
print(testCase1, solution(testCase1))
print(testCase2, solution(testCase2))
print(testCase3, solution(testCase3))
print(testCase4, solution(testCase4))
print(testCase5, solution(testCase5))
print(testCase6, solution(testCase6))
'''
print(testCase7, solution(testCase7))

    


    