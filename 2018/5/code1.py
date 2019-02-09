def remove_at(i, s):
    return s[:i] + s[i+2:]

with open ("input.txt", "r") as inputfile:
    data=inputfile.readlines()
lastinput = ""
input = data[0].strip()
while lastinput != input:
    lastinput = input
    for i in range(0, len(input)-1):
        if (input[i].isupper() and input[i+1].islower()) or (input[i].islower() and input[i+1].isupper()):
            if input[i].lower() == input[i+1].lower():
                print input[i],input[i+1]
                input = remove_at(i,input)
                break


print input
print len(input)
