def intcode(program,noun,verb):
    program[1] = noun
    program[2] = verb
    position = 0
    while program[position] != 99:
        if program[position] == 1:
            program[program[position+3]] = program[program[position+1]] + program[program[position+2]]
        elif int(program[position]) == 2:
            program[program[position+3]] = program[program[position+1]] * program[program[position+2]]
        position +=4
    return program[0]
