list = []
with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
for line in data:
    list.append(int(line))

i=0
moves=0
while i>=0 and i<len(list):
	if list[i]>=3:
		list[i]-=1
		i+=(list[i]+1)
	else:
		list[i]+=1
		i+=(list[i]-1)
	moves+=1
print(moves)
