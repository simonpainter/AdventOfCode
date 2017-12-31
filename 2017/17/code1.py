#steps = 371
steps = 3
count = 0
position = 0
total = 2017
vortex = [0]

def move(vortex,steps,position):
    size = len(vortex)
    difference = steps % size
    if difference + position >= size:
        position = difference + position - size
    else:
        position += difference
    return position

while count < total:
    count += 1
    position = move(vortex,steps,position)
    vortex.insert(position+1, count)
    position += 1


print(vortex[vortex.index(2017)+1])
