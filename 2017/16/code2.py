dancers = list("abcdefghijklmnop")
history = ["".join(dancers)]
with open ("input.txt", "r") as inputfile:
    dance=inputfile.read().strip().split(",")
    for i in range(1,42):
        for step in dance:
            if step[0]=="s":
                spinval = int(step[1:])
                dancers = dancers[len(dancers)-spinval:] + dancers[:len(dancers)-spinval]
            elif step[0]=="x":
                exvals = step[1:].split("/")
                dancers[int(exvals[0])],dancers[int(exvals[1])] = dancers[int(exvals[1])],dancers[int(exvals[0])]
            elif step[0]=="p":
                pvals = step[1:].split("/")
                first = dancers.index(pvals[0])
                second = dancers.index(pvals[1])
                dancers[first],dancers[second] = dancers[second],dancers[first]
        if "".join(dancers) in history:
            break
        history.append("".join(dancers))
print(history[1000000000 % len(history)])
