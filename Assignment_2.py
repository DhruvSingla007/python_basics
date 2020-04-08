# Extracting all email IDs from text_2.txt

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "text_2.txt"

fh = open(fname)

count = 0

for line in fh:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        count = count + 1
        words = line.split()
        print(words[1])

print(count)