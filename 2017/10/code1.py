with open ("input.txt", "r") as inputfile:
        data=inputfile.read()
steps = []
for item in data.split(","):
    steps.append(int(item.strip()))
chainlength = 256
chain = range(chainlength)
increment = 0
position = 0
shifts = []
def shift(l, n):
    return l[n:] + l[:n]

for step in steps:
    twist = chain[position:step]
    remainder = chain[step:]
    chain = twist[::-1]+remainder
    n=step+increment
    if n >= chainlength:
        n=n-chainlength
    print n
    shifts.append(n)
    chain=shift(chain,(n))
    increment +=1

for change in shifts:
    chain = shift(chain,-change)
print chain
print chain[0]*chain[1]
