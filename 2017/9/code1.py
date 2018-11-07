with open ("input.txt", "r") as inputfile:
        data=inputfile.read()

i=0
depth = 0
total = 0
garbage = 0
while i<len(data):
    if data[i]=="<":
        i+=1
        #enter the garbage loop
        while data[i]!=">":
            if data[i]=="!":
                i+=2
            else:
                i+=1
                garbage +=1
    if data[i]=="{":
        depth +=1
    if data[i]=="}":
        total+=depth
        depth -=1



    print(data[i])
    i+=1

print(depth)
print(total)
print(garbage)
