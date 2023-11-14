"""
INSTRUCTION BITS:
0 - ALU Register A: Enable Input
1 - ALU Add: Enable Out
2 - ALU Subtract: Enable Out
3 - ALU Multiply: Enable Out
4 - ALU Divide: Enable Out
5 - ALU Register B: Enable Input

6 - COUNTER: Enable Count
7 - COUNTER: Jump/enable INPUT (Sets value)
8 - COUNTER: Output Enable

9 - MAR: Enable Input

10 - RAM: Enable Input
11 - RAM: Enable Output

12 - IR: Enable Output
13 - IR: Enable Input

14 - Instruction Counter: Reset

15 - Display: Enable Input

16 - HALT
"""
from typing import List

class OPCODE:
    def __init__(self,code: str):
        self.code: str = code

        self.instructions: List[int] = []

        self.reset()
        self.alu_register_a_enable_input: int = 31
        self.alu_add_enable_out: int = 30
        self.alu_subtract_enable_out: int = 29
        self.alu_multiply_enable_out: int = 28
        self.alu_divide_enable_out: int = 27
        self.alu_register_b_enable_input: int = 26
        self.counter_enable_count: int = 25
        self.counter_jump_enable_input: int = 24
        self.counter_output_enable: int = 23
        self.mar_enable_input: int = 22
        self.ram_enable_input: int = 21
        self.ram_enable_output: int = 20
        self.ir_enable_output: int = 19
        self.ir_enable_input: int = 18
        self.instr_counter_reset: int = 17
        self.display_enable_input: int = 16
        self.halt: int = 15

    def reset(self) -> None:
        self.instr_bits: List[int] = [0 for i in range(32)]

    def addCode(self,reset:bool =True) -> None:
        instruction:str = ""
        for i in self.instr_bits:
            instruction += str(i)
        if reset:
            self.reset()
        self.instructions.append(instruction)
    
    def prepare(self) -> None:
        self.reset()
        #Counter Out, MAR In
        self.instr_bits[self.counter_output_enable] = 1
        self.instr_bits[self.mar_enable_input] = 1
        self.addCode()
        #RAM Out, IR In, Counter Enable
        self.instr_bits[self.ram_enable_output] = 1
        self.instr_bits[self.ir_enable_input] = 1
        self.instr_bits[self.counter_enable_count] = 1
        self.addCode()

    def getInstructions(self) -> List[str]:
        return self.instructions
    
    def finalize(self) -> None:
        # TODO: check if this is working
        self.instr_bits[self.instr_counter_reset] = 1
        self.addCode()
    
    def getOpcode(self) -> str:
        return self.code

#HALT PROGRAM
class HLT(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #HALT
        self.instr_bits[self.halt] = 1
        self.addCode()
        self.finalize()

#Load A Register from RAM
class LDA(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #IR Out, MAR In
        self.instr_bits[self.ir_enable_output] = 1
        self.instr_bits[self.mar_enable_input] = 1
        self.addCode()
        #RAM Out, A In
        self.instr_bits[self.ram_enable_output] = 1
        self.instr_bits[self.alu_register_a_enable_input] = 1
        self.addCode()
        self.finalize()

#Load B Register from RAM
class LDB(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #IR Out, MAR In
        self.instr_bits[self.ir_enable_output] = 1
        self.instr_bits[self.mar_enable_input] = 1
        self.addCode()
        #RAM Out, B In
        self.instr_bits[self.ram_enable_output] = 1
        self.instr_bits[self.alu_register_b_enable_input] = 1
        self.addCode()
        self.finalize()

#Add Instruction - Send Sum to display
class SUM(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #SUM Out, Display In
        self.instr_bits[self.alu_add_enable_out] = 1
        self.instr_bits[self.display_enable_input] = 1
        self.addCode()
        self.finalize()

#Subtract Instruction - Send Difference to display
class SUB(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #SUB Out, Display In
        self.instr_bits[self.alu_subtract_enable_out] = 1
        self.instr_bits[self.display_enable_input] = 1
        self.addCode()
        self.finalize()

#Multiply Instruction - Send Product to display
class MLT(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #MLT Out, Display In
        self.instr_bits[self.alu_multiply_enable_out] = 1
        self.instr_bits[self.display_enable_input] = 1
        self.addCode()
        self.finalize()

#Divide Instruction - Send Divident to display
class DIV(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #DIV Out, Display In
        self.instr_bits[self.alu_divide_enable_out] = 1
        self.instr_bits[self.display_enable_input] = 1
        self.addCode()
        self.finalize()

#Jump Instruction - Set Program Counter to value in RAM
class JMP(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #IR Out, MAR In
        self.instr_bits[self.ir_enable_output] = 1
        self.instr_bits[self.mar_enable_input] = 1
        self.addCode()
        #RAM Out, Counter In
        self.instr_bits[self.ram_enable_output] = 1
        self.instr_bits[self.counter_jump_enable_input] = 1
        self.addCode()
        self.finalize()

#Reset Instruction Counter
class ICR(OPCODE):
    def __init__(self,opcode: str):
        super().__init__(opcode)
        self.prepare()
        #Counter Reset
        self.instr_bits[self.instr_counter_reset] = 1
        self.addCode()
        self.finalize()
   










    







    

