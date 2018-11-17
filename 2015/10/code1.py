import re

input = "1321131112"

for step in range(50):
    regex = re.compile(r"(([0-9])\2*)")
    output = regex.findall(input)
    input = ""
    for each in output:
        input = input + str(len(each[0])) + each[1]
    print step,len(input)
