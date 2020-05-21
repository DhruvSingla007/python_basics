def solution(times, times_limit):
    # Your code here
    ansArr = []
    ansArr.append(max(times_limit, times_limit - times[0][len(times) -1]))
    
    for i in range(1,len(times) - 1,1):
        ansArr.append(times[i][len(times) - 1] + times[len(times) -1][i])
    
    print(ansArr)

    possible_outputs = [[]]

    total = ansArr[0]
    maxSize = 0

    for i in range(1, len(ansArr), 1):
      if ansArr[i] > total:
        continue
      
      op = []
      op.append((ansArr[i], i))
      print("option", op)
      sum = ansArr[i]
      for j in range(i+1, len(ansArr), 1):
        if ansArr[j] > total:
          continue
        if sum + ansArr[j] > total:
          if len(op) > maxSize:
            possible_outputs.append(op)
            maxSize = len(op)
          print("possible" ,possible_outputs)
          break
        
        op.append((ansArr[j], j))
        sum += ansArr[j]

      if sum <= total and len(op) > maxSize:
        maxSize = len(op)
        possible_outputs.append(op)

      print("outputs: ", possible_outputs)

      if maxSize == 0:
        return []
      
      final = []
      for l in possible_outputs:
        if (len(l) == maxSize):
          final = l
          break
      
      #print('final',final)
      ans = []

      for (t,position) in final:
        ans.append(position - 1)
      
    return ans


times = [
  [0, 2, 2, 2, -1],  # 0 = Start
  [9, 0, 2, 2, -1],  # 1 = Bunny 0
  [9, 3, 0, 2, -1],  # 2 = Bunny 1
  [9, 3, 2, 0, -1],  # 3 = Bunny 2
  [9, 3, 2, 2,  0],  # 4 = Bulkhead
]

times_limit = 1

ans = solution(times, times_limit)

print(ans)
      