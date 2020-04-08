a = [1,2,3,'dhruv','swati']

for el in a:
    print(el)


# slicing in lists
b = a[2:4]
c = a[4:2]
print('b',b)
print('c',c)

# build a list from scratch
stuff = list()
stuff.append("dhruv")
stuff.append('singla')
stuff.append("Swati")
stuff.pop()

for el in stuff:
    print(el)

nums = [5,4,6,2,8,3,1,9]

# sorting a list
nums.sort()
print(nums)

# length of list
print("Length :",len(nums))

# maximum and minimum of list
print('Max :', max(nums))
print('Min :', min(nums))

# sum of list
print("Sum : ",sum(nums))


# LISTS AND STRINGS

abc = "Hi, my name is Dhruv Singla"
stringList = abc.split()
print(stringList)

favourableList = abc.split(',')
print(favourableList)

favourableList = abc.split('m')
print(favourableList)

# example of extracting name from the string given below
message = "From dhruvsingla@gmail.com delivered on 5:30pm on Thursday"
pieces = message.split()
email = pieces[1]
pieces_2 = email.split('@')
name = pieces_2[0]

print(name)

# adding two lists
x = [1,2,3]
y = [5,6,7]
z = x+y
print(z)