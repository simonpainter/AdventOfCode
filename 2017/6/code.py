memory = []
history = []
with open ("input.txt", "r") as inputfile:
	data=inputfile.readlines()
temp = data[0].split("\t")
for block in temp:
	memory.append(int(block.strip()))
history.append(memory[:])

count = 0

while sorted(list(set(map(tuple,history))))==sorted(list(map(tuple,history))):
    i = memory.index(max(memory))
    blocks = memory[i]
    memory[i]=0
    while blocks > 0:
        i+=1
        if i>=len(memory):
            i -= len(memory)
        memory[i] +=1
        blocks -=1
    history.append(memory[:])
    count+=1
search = history[-1]
print(search)
print(history)
print(count)
print(len(history)-(history.index(search)+1))
