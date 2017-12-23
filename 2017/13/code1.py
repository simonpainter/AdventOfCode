firewall = {}
with open ("testinput.txt", "r") as inputfile:
    lines=inputfile.readlines()
    for line in lines:
        data = line.strip().split(":")
        firewall[int(data[0])] = data[1]
