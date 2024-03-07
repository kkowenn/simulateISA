class CPU:
    def __init__(self, initial_register_values):
        self.registers = initial_register_values
        self.memory = [0] * 1024
        self.mul_result = 0
        self.pc = 0

    def mov(self, dest_reg, value):
        self.registers[dest_reg] = value
        self.memory[dest_reg] = value

    def add(self, dest_reg, src_reg, value):
        result = self.registers[src_reg] + value
        self.registers[dest_reg] = result
        self.memory[dest_reg] = result

    def sub(self, dest_reg, src_reg, value):
        result = self.registers[src_reg] - value
        self.registers[dest_reg] = result
        self.memory[dest_reg] = result

    def mul(self, dest_reg, src_reg, value):
        result = self.registers[src_reg] * value
        self.registers[dest_reg] = result
        self.memory[dest_reg] = result

    def div(self, dest_reg, src_reg, value):
        if value == 0:
            raise ValueError("Division by zero")
        quotient = self.registers[src_reg] // value
        remainder = self.registers[src_reg] % value
        self.mul_result = remainder
        self.registers[dest_reg] = quotient
        self.memory[dest_reg] = quotient

    def lshift(self, dest_reg, src_reg, value):
        result = self.registers[src_reg] << value
        self.registers[dest_reg] = result
        self.memory[dest_reg] = result

    def rshift(self, dest_reg, src_reg, value):
        result = self.registers[src_reg] >> value
        self.registers[dest_reg] = result
        self.memory[dest_reg] = result

    def execute_instruction(self, opcode, dest_reg, src_or_dest_reg, reg_or_value):
        # Check if reg_or_value is a register or an immediate value
        if isinstance(reg_or_value, str) and reg_or_value.startswith('R'):
            value_index = int(reg_or_value[1:])
            value = self.registers[value_index]
        else:
            value = int(reg_or_value)
        if opcode == "mov":
            self.mov(dest_reg, value)
        else:
            if hasattr(self, opcode):
                # Ensure src_or_dest_reg is correctly used as per each instruction's expectation
                getattr(self, opcode)(dest_reg, src_or_dest_reg, value)
            else:
                print(f"Unknown opcode: {opcode}")

    def execute_program(self, program):
        for instruction in program:
            self.execute_instruction(*instruction)

    def print_registers(self):
        for i, value in enumerate(self.registers):
            # Format the value as a 32-bit signed integer in binary
            formatted_value = format(value & 0xffffffff, '032b')
            print(f"R{i}: {value} [{formatted_value}]")

    def print_memory(self):
        for i, value in enumerate(self.memory):
            if value != 0:
                # Format the value as a 32-bit signed integer in binary
                formatted_value = format(value & 0xffffffff, '032b')
                print(f"mem[{i}]: {value} [{formatted_value}]")


def main():
    print("Enter initial values for r0 to r7 (space-separated):")
    initial_register_values = list(map(int, input().strip().split()))
    cpu = CPU(initial_register_values)

    print("Values of registers:")
    cpu.print_registers()

    program = []
    print("Instructions available: mov, add, sub, mul, div, lshift, rshift")
    print("Enter program instructions (e.g., add R1 R2 3). Input 'e' on a new line to execute:")
    input_lines = []

    while True:
        instruction = input().strip()
        if instruction.lower() == 'e':
            break
        input_lines.append(instruction)

    for instruction in input_lines:
        tokens = instruction.split()
        if len(tokens) != 4:
            print(f"Invalid instruction format: {instruction}. Please try again.")
            continue
        opcode, dest_reg, src_or_dest_reg, reg_or_value = tokens

        if not dest_reg.startswith("R"):
            print("Invalid destination register. Registers should start with 'R'.")
            continue
        try:
            dest_reg_index = int(dest_reg[1:])
            src_or_dest_reg_index = int(src_or_dest_reg[1:]) if src_or_dest_reg.startswith("R") else src_or_dest_reg
            program.append((opcode, dest_reg_index, src_or_dest_reg_index, reg_or_value))
        except ValueError:
            print("Invalid register index or value. Please enter integers for register indexes.")
            continue

    if not program:
        print("No instructions provided. Exiting.")
        return

    cpu.execute_program(program)
    print("\nValues of registers:")
    cpu.print_registers()
    print("\nValues of memory:")
    cpu.print_memory()
    print("\nCPI (Clocks Per Instruction):")
    cpi = len(program)
    print(f"CPI = {cpi}")

if __name__ == "__main__":
    main()
