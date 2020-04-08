# input function always returns a string

name = input("Enter your name")

print("Welcome", name)
# ',' for the next word and the space is added
print("Welcome", name,)

# will give error cant't compare a string and int
score = input("Enter Score : ")

if score > 10:
    print("Greater")