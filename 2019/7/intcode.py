class IntCodeComputer:
    def __init__(self, program, input_values=None):
        self.memory = program.copy()
        self.ip = 0  # shorter name for instruction pointer
        self.input_values = list(input_values) if input_values is not None else []
        self.outputs = []

    def reset(self, program):
        self.memory = program.copy()
        self.ip = 0
        self.input_values.clear()
        self.outputs.clear()

    def add_input(self, value):
        # Handle both single values and lists
        if isinstance(value, list):
            self.input_values.extend(value)
        else:
            self.input_values.append(value)

    def execute(self):
        mem = self.memory  # local reference for faster access
        while True:
            instr = mem[self.ip]
            op = instr % 100
            
            if op == 99:
                break
                
            # Get modes for up to 3 parameters
            modes = instr // 100
            mode1 = modes % 10
            mode2 = (modes // 10) % 10
            
            # Use local variables for faster access
            ip = self.ip
            
            if op == 1:  # add
                v1 = mem[mem[ip + 1]] if mode1 == 0 else mem[ip + 1]
                v2 = mem[mem[ip + 2]] if mode2 == 0 else mem[ip + 2]
                mem[mem[ip + 3]] = v1 + v2
                self.ip += 4
            elif op == 2:  # multiply
                v1 = mem[mem[ip + 1]] if mode1 == 0 else mem[ip + 1]
                v2 = mem[mem[ip + 2]] if mode2 == 0 else mem[ip + 2]
                mem[mem[ip + 3]] = v1 * v2
                self.ip += 4
            elif op == 3:  # input
                if not self.input_values:
                    raise ValueError("No input values available")
                mem[mem[ip + 1]] = self.input_values.pop(0)
                self.ip += 2
            elif op == 4:  # output
                v1 = mem[mem[ip + 1]] if mode1 == 0 else mem[ip + 1]
                self.outputs.append(v1)
                self.ip += 2
            elif op == 5:  # jump-if-true
                v1 = mem[mem[ip + 1]] if mode1 == 0 else mem[ip + 1]
                v2 = mem[mem[ip + 2]] if mode2 == 0 else mem[ip + 2]
                self.ip = v2 if v1 != 0 else ip + 3
            elif op == 6:  # jump-if-false
                v1 = mem[mem[ip + 1]] if mode1 == 0 else mem[ip + 1]
                v2 = mem[mem[ip + 2]] if mode2 == 0 else mem[ip + 2]
                self.ip = v2 if v1 == 0 else ip + 3
            elif op == 7:  # less than
                v1 = mem[mem[ip + 1]] if mode1 == 0 else mem[ip + 1]
                v2 = mem[mem[ip + 2]] if mode2 == 0 else mem[ip + 2]
                mem[mem[ip + 3]] = 1 if v1 < v2 else 0
                self.ip += 4
            elif op == 8:  # equals
                v1 = mem[mem[ip + 1]] if mode1 == 0 else mem[ip + 1]
                v2 = mem[mem[ip + 2]] if mode2 == 0 else mem[ip + 2]
                mem[mem[ip + 3]] = 1 if v1 == v2 else 0
                self.ip += 4