# in is a membership operator
# range() is a function that returns a sequence of numbers
# i is a variable that will hold the value of the current number in the sequence

for i in range(5):  # this will loop 5 times
    print(i)

for a in range(1, 6):
    print(a)

for b in range(1, 6, 2):
    print(b)
    
# print same thing multiple times
for i in range(1,6):
    print("hello")

for j in range(5):
    print(j,end=" ")

# break 
for i in range(10):
    if i == 5:
        break
    print(i)

# continue
for i in range(1,5):
    if i == 3:
        continue
    print(i, end=" ")

# loop with input
for i in range(3):
    name = input("Enter your name: ")
    print("hello",name)