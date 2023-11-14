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
    def __init__(self,code):
        self.code = code

        self.instructions = []

        self.reset()
        self.alu_register_a_enable_input = 31
        self.alu_add_enable_out = 30
        self.alu_subtract_enable_out = 29
        self.alu_multiply_enable_out = 28
        self.alu_divide_enable_out = 27
        self.alu_register_b_enable_input = 26
        self.counter_enable_count = 25
        self.counter_jump_enable_input = 24
        self.counter_output_enable = 23
        self.mar_enable_input = 22
        self.ram_enable_input = 21
        self.ram_enable_output = 20
        self.ir_enable_output = 19
        self.ir_enable_input = 18
        self.instr_counter_reset = 17
        self.display_enable_input = 16
        self.halt = 15

    def reset(self):
        self.instr_bits = [0 for i in range(32)]

    def addCode(self,reset=True):
        instruction = ""
        for i in self.instr_bits:
            instruction += str(i)
        if reset:
            self.reset()
        self.instructions.append(instruction)
    
    def prepare(self):
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

    def getInstructions(self):
        return self.instructions
    
    def finalize(self):
        # TODO: check if this is working
        self.instr_bits[self.instr_counter_reset] = 1
        self.addCode()
    
    def getOpcode(self):
        return self.code

#HALT PROGRAM
class HLT(OPCODE):
    def __init__(self,opcode):
        super().__init__(opcode)
        self.prepare()
        #HALT
        self.instr_bits[self.halt] = 1
        self.addCode()
        self.finalize()

#Load A Register from RAM
class LDA(OPCODE):
    def __init__(self,opcode):
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
    def __init__(self,opcode):
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
    def __init__(self,opcode):
        super().__init__(opcode)
        self.prepare()
        #SUM Out, Display In
        self.instr_bits[self.alu_add_enable_out] = 1
        self.instr_bits[self.display_enable_input] = 1
        self.addCode()
        self.finalize()

#Subtract Instruction - Send Difference to display
class SUB(OPCODE):
    def __init__(self,opcode):
        super().__init__(opcode)
        self.prepare()
        #SUB Out, Display In
        self.instr_bits[self.alu_subtract_enable_out] = 1
        self.instr_bits[self.display_enable_input] = 1
        self.addCode()
        self.finalize()

#Multiply Instruction - Send Product to display
class MLT(OPCODE):
    def __init__(self,opcode):
        super().__init__(opcode)
        self.prepare()
        #MLT Out, Display In
        self.instr_bits[self.alu_multiply_enable_out] = 1
        self.instr_bits[self.display_enable_input] = 1
        self.addCode()
        self.finalize()

#Divide Instruction - Send Divident to display
class DIV(OPCODE):
    def __init__(self,opcode):
        super().__init__(opcode)
        self.prepare()
        #DIV Out, Display In
        self.instr_bits[self.alu_divide_enable_out] = 1
        self.instr_bits[self.display_enable_input] = 1
        self.addCode()
        self.finalize()

#Jump Instruction - Set Program Counter to value in RAM
class JMP(OPCODE):
    def __init__(self,opcode):
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
    def __init__(self,opcode):
        super().__init__(opcode)
        self.prepare()
        #Counter Reset
        self.instr_bits[self.instr_counter_reset] = 1
        self.addCode()
        self.finalize()


class BIOS:
    def __init__(self,output_file=None):
        self.output_file = output_file
        self.opcodes: List[OPCODE] = []
        self.op_LDA = LDA("0000000000000000")
        self.op_LDB = LDB("0000000000000001")
        self.op_SUM = SUM("0000000000000010")
        self.op_SUB = SUB("0000000000000011")
        self.op_MLT = MLT("0000000000000100")
        self.op_DIV = DIV("0000000000000101")
        self.op_JMP = JMP("0000000000000110")
        self.op_ICR = ICR("0000000000000111")
        self.op_HLT = HLT("0000000000001000")
        self.opcodes.append(self.op_LDA)
        self.opcodes.append(self.op_LDB)
        self.opcodes.append(self.op_SUM)
        self.opcodes.append(self.op_SUB)
        self.opcodes.append(self.op_MLT)
        self.opcodes.append(self.op_DIV)
        self.opcodes.append(self.op_JMP)
        self.opcodes.append(self.op_ICR)
        self.opcodes.append(self.op_HLT)

        self.ROM_data_binary = {}
        for opcode in self.opcodes:
            steps = []
            instructions = opcode.getInstructions()
            for instruction in instructions:
                steps.append(instruction)

            code = opcode.getOpcode()
            for i in range(len(steps)):
                #convert i to binary address of 8 digits
                address = code + bin(i)[2:].zfill(8)
                self.ROM_data_binary[address] = steps[i]
        for data in self.ROM_data_binary:
            print(data,self.ROM_data_binary[data])
        self.ROM_data_hex = {}
        for entry in self.ROM_data_binary:
            address = hex(int(entry,2))[2:].zfill(4)
            data = hex(int(self.ROM_data_binary[entry],2))[2:].zfill(8)
            self.ROM_data_hex[address] = data
    
    def writeBios(self):
        #write the data
        if not self.output_file:
            return None
        with open(self.output_file, "w") as f:
            f.write("v3.0 hex words addressed\n")
            for address in self.ROM_data_hex:
                data = self.ROM_data_hex[address]
                f.write(address + " " + data + "\n")
        
class Programmer:
    def __init__(self,output_path = None):
        self.bios = BIOS()
        self.address_index = 0
        self.default_value = "0000000000000000"
        self.operations = {}
        self.output_path = output_path
        self.RAM_hex_output = {}

    def addOperation(self,operation,value=None):
        data = {}
        if value:
            value = bin(value)[2:].zfill(16)
        data['value'] = value

        if operation == "LDA":
            data['opcode'] = self.bios.op_LDA.getOpcode()
        elif operation == "LDB":
            data['opcode'] = self.bios.op_LDB.getOpcode()
        elif operation == "SUM":
            data['opcode'] = self.bios.op_SUM.getOpcode()
        elif operation == "SUB":
            data['opcode'] = self.bios.op_SUB.getOpcode()
        elif operation == "MLT":
            data['opcode'] = self.bios.op_MLT.getOpcode()
        elif operation == "DIV":
            data['opcode'] = self.bios.op_DIV.getOpcode()
        elif operation == "JMP":
            data['opcode'] = self.bios.op_JMP.getOpcode()
        elif operation == "ICR":
            data['opcode'] = self.bios.op_ICR.getOpcode()
        elif operation == "HLT":
            data['opcode'] = self.bios.op_HLT.getOpcode()        
        else:
            return None
        self.operations[self.address_index] = data
        self.address_index += 1

    def add(self,a,b):
        self.addOperation("LDA",a)
        self.addOperation("LDB",b)
        self.addOperation("SUM")

    def subtract(self,a,b):
        self.addOperation("LDA",a)
        self.addOperation("LDB",b)
        self.addOperation("SUB")

    def multiply(self,a,b):
        self.addOperation("LDA",a)
        self.addOperation("LDB",b)
        self.addOperation("MLT")

    def divide(self,a,b):
        self.addOperation("LDA",a)
        self.addOperation("LDB",b)
        self.addOperation("DIV")

    def compile(self,auto_halt=True):
        if auto_halt:
            self.addOperation("HLT")
        RAM_binary = {}
        for address in self.operations:
            data = self.operations[address]
            opcode = data['opcode']
            value = data['value']
            if value:
                self.bios.ROM_data_binary[opcode + bin(address)[2:].zfill(8)] = value
                pointer = bin(self.address_index)[2:].zfill(16)
                RAM_binary[pointer] = value
                self.address_index += 1
                value = pointer
            else:
                value = self.default_value
            address = bin(address)[2:].zfill(16)
            RAM_binary[address] = opcode + value
        for address in RAM_binary:
            self.RAM_hex_output[hex(int(address,2))[2:].zfill(4)] = hex(int(RAM_binary[address],2))[2:].zfill(5)
        for address in self.RAM_hex_output:
            print(address,self.RAM_hex_output[address])

    def writeProgram(self):
        if not self.output_path:
            return None
        with open(self.output_path, "w") as f:
            f.write("v3.0 hex words addressed\n")
            for address in self.RAM_hex_output:
                data = self.RAM_hex_output[address]
                f.write(address + " " + data + "\n")

            
############### write the bios ################
bios = BIOS("bios_24bit_hex_v1")
#bios.writeBios()
############### write the program #############
#pgm = Programmer("RAM_program_32bit_hex_v1")
pgm = Programmer("RAM_full_math_test")
pgm.add(25,50) #75
pgm.subtract(100,44) #56
pgm.multiply(12,12) #144
pgm.divide(100,5) #20
pgm.compile()
pgm.writeProgram()








    







    

