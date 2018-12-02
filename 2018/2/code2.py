import itertools

def compare(first, second):
    count = 0
    for i in range(len(first)):
        if first[i]!=second[i]:
            count+=1


    if count == 1:
        return first,second
    else:
        return 0


with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()

for pair in list(itertools.combinations(data,2)):
    if compare(pair[0], pair[1]):
        print pair[0],pair[1]
