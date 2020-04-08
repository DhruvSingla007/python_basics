x = (1,2,3)
print(x)

(a,b) = (1,2)
print(a)
print(b)

# tuples are lists but immutble
# x[2] = 'd'

dct = {
    'a' : 1,
    'c' : 3,
    'e' : 5,
    'b' : 2,
    'd' : 4,
}

tplList = dct.items()

for (k,v) in tplList:
    print(k,v)

# sorting the list of tuples

# deafult sorting is done according to key

# ascending order
print(tplList)
print(sorted(tplList))

for (k,v) in sorted(tplList):
    print(k,v)

# descending order
for (k,v) in sorted(tplList,reverse = True):
    print(k,v)

# sorting according to the values
reverseList = list()
for (k,v) in tplList:
    reverseList.append((v,k))

print(reverseList)

for (v,k) in sorted(reverseList,reverse = True):
    print(k,v)


