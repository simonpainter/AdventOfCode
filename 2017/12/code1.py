pipes = {}

with open ("testinput.txt", "r") as inputfile:
    lines=inputfile.readlines()
    for line in lines:
        values = line.strip().split("<->")
        pipes[values[0]]=values[1].split(",")
