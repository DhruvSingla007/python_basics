# key - value pairs

purse = dict()
purse['money'] = 12
purse['candy'] = 10
purse['tissues'] = 15
purse[2] = 16

print(purse)
print(purse[2])
print(purse['money'])

for el in purse:
    print(el)

# python will give error if we are accessing the kry that is not present in the dictionary
# in order to remove the above restiction 'get' keyword is used which sets the given default value

counts = dict()
names = ['ds','ht','ps','ad','sm','ds','ds','ht']
for name in names:
    counts[name] = counts.get(name,0) + 1

print(counts)

# above code is similar to 
counts_2 = dict()
for name in names:
    if not name in counts_2:
        counts_2[name] = 1
        continue
    else:
        counts_2[name] = counts_2[name] + 1

print(counts_2)

# converting dictionaries into lists
myDict = {
    'a':1,
    'b':2,
    'c':3,
}

print(myDict)
keyList = myDict.keys()
print('Keys List :\n',keyList,'\n')

valueList = myDict.values()
print('Values List :\n',valueList,'\n')

tupleList = myDict.items()
print('Tuple List :\n',tupleList,'\n')

# TWO ITERATION VARIABLES

for k,val in myDict.items():
    print(k,val)
