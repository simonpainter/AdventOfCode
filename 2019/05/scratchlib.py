import time
def intcode(program,input):
    position = 0
    while program[position][-2:] != '99':
        opcode = str(program[position]).zfill(5)
        if int(opcode[-2:]) == 1:
            if int(opcode[-3:-2]) == 0:
                p1=program[int(program[position+1])]
            else:
                p1=program[position+1]
            if int(opcode[-4:-3]) == 0:
                p2=program[int(program[position+2])]
            else:
                p2=program[position+2]
            program[int(program[position+3])] = str(int(p1) + int(p2))
            position += 4
        elif int(opcode[-2:]) == 2:
            if int(opcode[-3:-2]) == 0:
                p1=program[int(program[position+1])]
            else:
                p1=program[position+1]
            if int(opcode[-4:-3]) == 0:
                p2=program[int(program[position+2])]
            else:
                p2=program[position+2]
            program[int(program[position+3])] = str(int(p1) * int(p2))
            position += 4
        elif int(opcode[-2:]) == 3:
            program[int(program[position+1])] = input
            position += 2
        elif int(opcode[-2:]) == 4:
            output = program[int(program[position+1])]
            print(output)
            print program[position-1:position+6]
            position += 2
    return program[position][-2:]
