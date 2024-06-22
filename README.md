# CPU Simulation Program

### Overview
This program simulates a simple CPU with basic arithmetic and bitwise operations. It initializes CPU registers with user-provided values and executes a series of instructions entered by the user. The program supports the following operations: `mov`, `add`, `sub`, `mul`, `div`, `lshift`, and `rshift`. It outputs the state of the CPU registers and memory before and after executing the instructions.

### Initial Setup
1. **Register Initialization**:
   - The program prompts the user to enter initial values for registers R0 to R7.
   - These values are stored in the CPU's registers and memory.

### Instructions Supported
- **mov**: Move an immediate value to a register.
- **add**: Add an immediate value to the value in a source register and store the result in a destination register.
- **sub**: Subtract an immediate value from the value in a source register and store the result in a destination register.
- **mul**: Multiply the value in a source register by an immediate value and store the result in a destination register.
- **div**: Divide the value in a source register by an immediate value, store the quotient in a destination register, and store the remainder in a special `mul_result` attribute.
- **lshift**: Left shift the value in a source register by an immediate value and store the result in a destination register.
- **rshift**: Right shift the value in a source register by an immediate value and store the result in a destination register.

### Program Execution
1. **Instruction Entry**:
   - The user enters program instructions line by line in the format `<opcode> <dest_reg> <src_reg> <value>`.
   - Instructions are added to the program until the user inputs 'e' to execute.

2. **Instruction Format Validation**:
   - Instructions must have exactly four tokens: opcode, destination register, source register (or immediate value), and immediate value (or register).
   - Destination and source registers must start with 'R' and be followed by an integer index.

3. **Instruction Execution**:
   - The CPU executes each instruction in the order entered.
   - If an invalid instruction is encountered, it is skipped with an error message.

### Output
- **Register Values**:
  - The program prints the values of all registers before and after program execution.
  - Values are displayed in both decimal and 32-bit binary format.
  
- **Memory Values**:
  - The program prints the values stored in memory that are non-zero.
  - Values are displayed in both decimal and 32-bit binary format.
  
- **CPI (Clocks Per Instruction)**:
  - The program calculates and prints the CPI based on the number of instructions executed.

### Example Usage
1. Run the program.
2. Enter initial register values (space-separated) for R0 to R7.
3. Enter program instructions (e.g., `add R1 R2 3`). Input 'e' on a new line to execute.
4. View the state of registers and memory before and after execution.
5. View the calculated CPI.

### Note
- Division by zero is handled with an error message.
- The program does not handle invalid opcodes or register indices gracefully and may terminate unexpectedly if such cases are encountered.

This program provides a basic simulation of a CPU and is intended for educational purposes to understand CPU operations and instruction execution.
