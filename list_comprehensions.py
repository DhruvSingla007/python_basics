# IMP : COOL : 
# LIST COMPREHENSIONS

c = {
    'a' : 10,
    'b' : 1,
    'c' : 22,
}

tupList = list()
for (k,v) in c.items():
    tupList.append((v,k))

print(tupList)

# the above code can be written in one line
tupList_2 = [(v,k) for (k,v) in c.items()]
print(tupList_2)

x,y = 3,4

print(y)