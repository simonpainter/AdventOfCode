import re
count = 0
p  = re.compile(r"(\d+).(\d+)")
with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

board = {}
for line in data:
    claim = line.strip().split(" ")
    this = p.findall(claim[2])[0]
    that = p.findall(claim[3])[0]
    print this, that
    for x in range(int(this[0]),int(this[0])+int(that[0])):
        for y in range(int(this[1]),int(this[1])+int(that[1])):
            map = str(x)+"x"+str(y)
            board[map]=0
for line in data:
    claim = line.strip().split(" ")
    this = p.findall(claim[2])[0]
    that = p.findall(claim[3])[0]
    print this, that
    for x in range(int(this[0]),int(this[0])+int(that[0])):
        for y in range(int(this[1]),int(this[1])+int(that[1])):
            map = str(x)+"x"+str(y)
            board[map]+=1

for line in data:
    claimvalid = 1
    claim = line.strip().split(" ")
    this = p.findall(claim[2])[0]
    that = p.findall(claim[3])[0]
    for x in range(int(this[0]),int(this[0])+int(that[0])):
        for y in range(int(this[1]),int(this[1])+int(that[1])):
            map = str(x)+"x"+str(y)
            if board[map]>1:
                claimvalid = 0
    if claimvalid == 1:
        print claim
