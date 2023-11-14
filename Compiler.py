from BIOS import BIOS

class Compiler:
    def __init__(self,output_path:str=None):
        self.bios:BIOS = BIOS()
        self.address_index:int = 0
        self.default_value:str = "0000000000000000"
        self.operations:dict = {}
        self.output_path:str = output_path
        self.RAM_hex_output:dict = {}

    def addOperation(self,operation:str,value:int=None) -> None:
        data:dict = {}
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

    def add(self,a:int,b:int) -> None:
        self.addOperation("LDA",a)
        self.addOperation("LDB",b)
        self.addOperation("SUM")

    def subtract(self,a:int,b:int) -> None:
        self.addOperation("LDA",a)
        self.addOperation("LDB",b)
        self.addOperation("SUB")

    def multiply(self,a:int,b:int) -> None:
        self.addOperation("LDA",a)
        self.addOperation("LDB",b)
        self.addOperation("MLT")

    def divide(self,a:int,b:int) -> None:
        self.addOperation("LDA",a)
        self.addOperation("LDB",b)
        self.addOperation("DIV")

    def compile(self,auto_halt:bool=True):
        if auto_halt:
            self.addOperation("HLT")
        RAM_binary:dict = {}
        for address in self.operations:
            data = self.operations[address]
            opcode:str = data['opcode']
            value:str = data['value']
            if value:
                self.bios.ROM_data_binary[opcode + bin(address)[2:].zfill(8)] = value
                pointer:str = bin(self.address_index)[2:].zfill(16)
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

    def writeProgram(self) -> None:
        if not self.output_path:
            return None
        with open(self.output_path, "w") as f:
            f.write("v3.0 hex words addressed\n")
            for address in self.RAM_hex_output:
                data:str = self.RAM_hex_output[address]
                f.write(f'{address} {data}\n')