#
xfile = open('hello.txt','r')
inp = xfile.read()

#print(inp[:20])


count = 0


for line in inp:
    count = count + 1
    #print(line)

print(count)


newFile = open('hello.txt','r')

# here the lines printed are having spaces between them as the print function adds a \n automatically
#for line in newFile:
    #if line.startswith('Dhruv'):
        #print(line)

# solution of the above problem

lines = 0

for line in newFile:
    lines = lines + 1
    line = line.rstrip()
    if line.startswith('Dhruv'):
        print(line)

print(lines)
