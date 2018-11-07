pipes = {}

with open ("testinput.txt", "r") as inputfile:
    lines=inputfile.readlines()
    for line in lines:
        values = line.split("<->")
        pipelist = []
        for pipe in values[1].split(","):
            pipelist.append(int(pipe.strip()))
        pipes[int(values[0].strip())]=pipelist



def followpipe(now,pathlist):
    for pipe in pipes[now]:
        if pipe in pathlist:
            pass
        else:
            pathlist.append(pipe)
            followpipe(pipe,pathlist)



pathlist = []
prog = 0

followpipe(prog,pathlist)

print(len(pathlist))
