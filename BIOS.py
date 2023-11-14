from OPCODES import *
from typing import List

class BIOS:
    def __init__(self,output_file:bool=None):
        self.output_file: str = output_file
        self.opcodes: List[OPCODE] = []
        self.op_LDA:OPCODE = LDA("0000000000000000")
        self.op_LDB:OPCODE = LDB("0000000000000001")
        self.op_SUM:OPCODE = SUM("0000000000000010")
        self.op_SUB:OPCODE = SUB("0000000000000011")
        self.op_MLT:OPCODE = MLT("0000000000000100")
        self.op_DIV:OPCODE = DIV("0000000000000101")
        self.op_JMP:OPCODE = JMP("0000000000000110")
        self.op_ICR:OPCODE = ICR("0000000000000111")
        self.op_HLT:OPCODE = HLT("0000000000001000")
        self.opcodes.append(self.op_LDA)
        self.opcodes.append(self.op_LDB)
        self.opcodes.append(self.op_SUM)
        self.opcodes.append(self.op_SUB)
        self.opcodes.append(self.op_MLT)
        self.opcodes.append(self.op_DIV)
        self.opcodes.append(self.op_JMP)
        self.opcodes.append(self.op_ICR)
        self.opcodes.append(self.op_HLT)

        self.ROM_data_binary: dict = {}
        self.ROM_data_hex: dict = {}

        for opcode in self.opcodes:
            steps: List[str] = []
            instructions: List[str] = opcode.getInstructions()
            for instruction in instructions:
                steps.append(instruction)

            code: str = opcode.getOpcode()
            for i in range(len(steps)):
                #convert i to binary address of 8 digits
                address: str = code + bin(i)[2:].zfill(8)
                self.ROM_data_binary[address] = steps[i]
        for data in self.ROM_data_binary:
            print(data,self.ROM_data_binary[data])
        for key in self.ROM_data_binary:
            address = hex(int(key,2))[2:].zfill(4)
            data: str = hex(int(self.ROM_data_binary[key],2))[2:].zfill(8)
            self.ROM_data_hex[address] = data
    
    def writeBios(self) -> None:
        #write the data
        if not self.output_file:
            return None
        with open(self.output_file, "w") as f:
            f.write("v3.0 hex words addressed\n")
            for address in self.ROM_data_hex:
                data = self.ROM_data_hex[address]
                f.write(address + " " + data + "\n")