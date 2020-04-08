# getting the mail fron the largest number of messages are sent
name = input("Enter file:")
if len(name) < 1 : name = "text_2.txt"
handle = open(name)

counts = dict()
for line in handle:
    if line.startswith('From:'):
        continue
    elif line.startswith('From'):
        words = line.split()
        if len(words) < 2:
            continue
        email = words[1]
        counts[email] = counts.get(email,0) + 1
        
name = None
ans = None

for email in counts:
    if name is None or counts[email] > counts[name]:
        name = email
        ans = counts[email]
        
print(name,ans)