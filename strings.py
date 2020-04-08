fruit = "banana"
print(fruit[5])


# length of the string
print(len(fruit))

index = 0
while index < len(fruit):
    print(index, fruit[index])
    index = index + 1


for letter in fruit:
    print(letter)

def a(string):
    count = 0
    for letter in string:
        if letter == 'a':
            count = count + 1
    return count

ans = a("banana")
print(ans)

# Slicing strings
s = "Dhruv Singla"
print(s[0:4])   # here 0 is included and 4 is not included

print(s[2:100])   # doesn't give any error

print(s[2:])   # will print upto the end

print(s[:8])   # will start printing from 0 upto 8(not included)

fruit = 'banana'

# 'in' keyword
print('n' in fruit)
print('nan' in fruit)

# 'lower' and 'upper' keywords
string_1 = "Hello There"
print(string_1.lower())
print(string_1.upper())

# 'replace' keyword
greet = "Hello World"
greet.replace('o','X') # will not replace as we have to store the changed value to another variable
print(greet)

changed = greet.replace('o','X')
print(changed)

nameChanged = greet.replace('World','Swati')
print(nameChanged)

# Stripping whitespaces
string_2 =  '    Hello World   '
print(string_2.lstrip()) # for stripping the left whitespace
print(string_2.rstrip()) # for stripping the right whitespace
print(string_2.strip()) # for stripping the both left and right whitespace

# print a required string
# let's say we want to extract swati from the string dhruv@swati.com
string_3 = "dhruv@swati.com"
atpos = string_3.find('@')
endPos = string_3.find('.',atpos+1)

print(string_3[atpos + 1 : endPos])

# new line char
stuff = 'Hello\nWorld'
print(stuff)
print(len(stuff))
