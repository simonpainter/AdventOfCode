# intcode.py

class IntCodeComputer:
    def __init__(self, program, input_values=None):
        # Make a copy of the program to avoid modifying original
        self.memory = program.copy()
        self.instruction_pointer = 0
        self.input_values = input_values if input_values is not None else []
        self.outputs = []
        
    def reset(self, program):
        """Reset computer to initial state with given program"""
        self.memory = program.copy()
        self.instruction_pointer = 0
        self.outputs = []
        
    def add_input(self, value):
        """Add input value to the queue"""
        self.input_values.append(value)
        
    def get_output(self):
        """Get list of all outputs"""
        return self.outputs
    
    def get_value(self, position):
        """Get value at memory position"""
        return self.memory[position]
    
    def set_value(self, position, value):
        """Set value at memory position"""
        self.memory[position] = value
    
    def get_parameter_value(self, param_num, instruction):
        """Get parameter value based on mode"""
        mode = (instruction // (10 ** (param_num + 1))) % 10
        param = self.memory[self.instruction_pointer + param_num]
        
        if mode == 0:  # Position mode
            return self.memory[param]
        else:  # Immediate mode
            return param
            
    def execute(self):
        """Execute the program until halt"""
        while True:
            instruction = self.memory[self.instruction_pointer]
            opcode = instruction % 100
            
            if opcode == 99:
                break
                
            if opcode == 1:  # Addition
                param1 = self.get_parameter_value(1, instruction)
                param2 = self.get_parameter_value(2, instruction)
                result_pos = self.memory[self.instruction_pointer + 3]
                self.memory[result_pos] = param1 + param2
                self.instruction_pointer += 4
                
            elif opcode == 2:  # Multiplication
                param1 = self.get_parameter_value(1, instruction)
                param2 = self.get_parameter_value(2, instruction)
                result_pos = self.memory[self.instruction_pointer + 3]
                self.memory[result_pos] = param1 * param2
                self.instruction_pointer += 4
                
            elif opcode == 3:  # Input
                if not self.input_values:
                    raise ValueError("No input values available")
                result_pos = self.memory[self.instruction_pointer + 1]
                self.memory[result_pos] = self.input_values.pop(0)
                self.instruction_pointer += 2
                
            elif opcode == 4:  # Output
                param1 = self.get_parameter_value(1, instruction)
                self.outputs.append(param1)
                self.instruction_pointer += 2
                
            elif opcode == 5:  # Jump-if-true
                param1 = self.get_parameter_value(1, instruction)
                param2 = self.get_parameter_value(2, instruction)
                if param1 != 0:
                    self.instruction_pointer = param2
                else:
                    self.instruction_pointer += 3
                    
            elif opcode == 6:  # Jump-if-false
                param1 = self.get_parameter_value(1, instruction)
                param2 = self.get_parameter_value(2, instruction)
                if param1 == 0:
                    self.instruction_pointer = param2
                else:
                    self.instruction_pointer += 3
                    
            elif opcode == 7:  # Less than
                param1 = self.get_parameter_value(1, instruction)
                param2 = self.get_parameter_value(2, instruction)
                result_pos = self.memory[self.instruction_pointer + 3]
                self.memory[result_pos] = 1 if param1 < param2 else 0
                self.instruction_pointer += 4
                
            elif opcode == 8:  # Equals
                param1 = self.get_parameter_value(1, instruction)
                param2 = self.get_parameter_value(2, instruction)
                result_pos = self.memory[self.instruction_pointer + 3]
                self.memory[result_pos] = 1 if param1 == param2 else 0
                self.instruction_pointer += 4
                
            else:
                raise ValueError(f"Unknown opcode: {opcode}")
        
        return self.memory[0]