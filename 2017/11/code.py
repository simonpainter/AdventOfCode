from collections import Counter
with open ("input.txt", "r") as inputfile:
        data=inputfile.read()

directions = (data.strip()).split(",")

x = 0
y = 0
z = 0
history = []
for direction in directions:
    if direction == "ne":
        x+=1
        z-=1
    elif direction == "nw":
        y+=1
        x-=1
    elif direction == "se":
        x+=1
        y-=1
    elif direction == "sw":
        z+=1
        x-=1
    elif direction == "n":
        y+=1
        z-=1
    elif direction == "s":
        z+=1
        y-=1
    history.append((abs(x)+abs(y)+abs(z))/2)

print(x)
print(y)
print(z)

print((abs(x)+abs(y)+abs(z))/2)
print(max(history))
