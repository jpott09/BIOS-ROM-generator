from BIOS import BIOS
from Compiler import Compiler

############### write the bios ################
bios_output_filename:str = "bios_test_24bit_hex_v1"
bios:BIOS = BIOS(bios_output_filename)
bios.writeBios()
############### write the program #############
ram_output_filename:str = "ram_test_32bit_hex_v1"
compiler:Compiler = Compiler(ram_output_filename)
compiler.add(25,50) #75
compiler.subtract(100,44) #56
compiler.multiply(12,12) #144
compiler.divide(100,5) #20
compiler.compile()
compiler.writeProgram()
