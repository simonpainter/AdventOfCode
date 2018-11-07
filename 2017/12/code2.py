pipes = {}

with open ("input.txt", "r") as inputfile:
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

groups = []

for starters in pipes.keys():
    pathlist = []
    followpipe(starters,pathlist)
    groups.append(sorted(pathlist))
unique_data = [list(x) for x in set(tuple(x) for x in groups)]

print(len(unique_data))
