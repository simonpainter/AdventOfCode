with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()


def do(this,that,what):
    this = this.strip().split(',')
    that = that.strip().split(',')
    for x in range(int(this[0]),int(that[0])+1):
        for y in range(int(this[1]),int(that[1])+1):
            if what == 'on':
                board[x][y]  +=1
            if what == 'off':
                board[x][y] -=1
                if board[x][y]<0:
                    board[x][y]=0
            if what == 'toggle':
                board[x][y] +=2

board = []
for x in range(0,1000):
    row = []
    for y in range(0,1000):
        row.append(0)
    board.append(row)

for line in data:
    words = line.split(" ")
    if words[1]=='on':
        this = words[2]
        that = words[4]
        do(this,that,words[1])
    elif words[1]=='off':
        this = words[2]
        that = words[4]
        do(this,that,words[1])
    else:
        this = words[1]
        that = words[3]
        do(this,that,words[0])

total = 0
for line in board:
    total += sum(line)


print total
