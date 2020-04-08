
name = input("Enter file:")
if len(name) < 1 : name = "text_2.txt"
handle = open(name)

counts = dict()

for line in handle:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        words = line.split(':')
        word = words[0].split()
        hour =  word[len(word)-1]
        counts[hour] = counts.get(hour,0) + 1

# print(counts)
revList = sorted(counts.items())
for (k,v) in revList:
    print(k,v)