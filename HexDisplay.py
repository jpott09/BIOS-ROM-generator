from typing import List

class HexDisplay:
    def __init__(self):
        self.top:int = 0
        self.top_left:int = 0
        self.top_right:int = 0
        self.mid:int = 0
        self.bottom_left:int = 0
        self.bottom_right:int = 0
        self.bottom:int = 0
        self.dec:int = 0

        self.bits: List[int] = [
            self.mid,
            self.top_left,
            self.top,
            self.top_right,
            self.bottom_left,
            self.bottom,
            self.bottom_right,
            self.dec
        ]


    """
    Segments:
                    0 (top)
    1 (top left)                2 (top right)
                    3 (middle)
    4 (bottom left)             5 (bottom right)
                    6 (bottom)
                                7 (decimal point)"""

    def reset(self) -> None:
        self.top = 0
        self.top_left = 0
        self.top_right = 0
        self.mid = 0
        self.bottom_left = 0
        self.bottom_right = 0
        self.bottom = 0
        self.dec = 0

    def refresh(self) -> str:
        self.bits = [
            self.mid,
            self.top_left,
            self.top,
            self.top_right,
            self.bottom_left,
            self.bottom,
            self.bottom_right,
            self.dec
        ]
        binary:str = ""
        for bit in self.bits:
            binary += str(bit)
        return binary
    
    def zero(self) -> str:
        self.reset()
        self.top = 1
        self.top_left = 1
        self.top_right = 1
        self.bottom_left = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def one(self) -> str:
        self.reset()
        self.top_right = 1
        self.bottom_right = 1
        return self.refresh()
    
    def two(self) -> str:
        self.reset()
        self.top = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_left = 1
        self.bottom = 1
        return self.refresh()
    
    def three(self) -> str:
        self.reset()
        self.top = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def four(self) -> str:
        self.reset()
        self.top_left = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_right = 1
        return self.refresh()
    
    def five(self) -> str:
        self.reset()
        self.top = 1
        self.top_left = 1
        self.mid = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def six(self) -> str:
        self.reset()
        self.top = 1
        self.top_left = 1
        self.mid = 1
        self.bottom_left = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def seven(self) -> str:
        self.reset()
        self.top = 1
        self.top_right = 1
        self.bottom_right = 1
        return self.refresh()
    
    def eight(self) -> str:
        self.reset()
        self.top = 1
        self.top_left = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_left = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def nine(self) -> str:
        self.reset()
        self.top = 1
        self.top_left = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_right = 1
        return self.refresh()
    
    def getDigit(self,digit: str) -> str:
        if digit == "0":
            return self.zero()
        elif digit == "1":
            return self.one()
        elif digit == "2":
            return self.two()
        elif digit == "3":
            return self.three()
        elif digit == "4":
            return self.four()
        elif digit == "5":
            return self.five()
        elif digit == "6":
            return self.six()
        elif digit == "7":
            return self.seven()
        elif digit == "8":
            return self.eight()
        elif digit == "9":
            return self.nine()
    
gen:HexDisplay = HexDisplay()
ROM_1:dict = {}
for i in range(0,999):
    #convert i to a hex address of 4 digits
    address:str = hex(i)[2:].zfill(4)
    digits: List[str] = [str(x) for x in str(i)]
    while len(digits) < 3:
        digits.insert(0,"0")
    #24 bit address
    digit_1:str = gen.getDigit(digits[0])
    digit_2:str = gen.getDigit(digits[1])
    digit_3:str = gen.getDigit(digits[2])
    data:str = digit_1 + digit_2 + digit_3
    ROM_1[address] = data

#output path 
ROM_1_path:str = "hex_ROM_24bit"

def writeROM(path:str, ROM:dict) -> None:
    with open(path, "w") as f:
        f.write("v3.0 hex words addressed\n")
        for address in ROM:
            data:str = ROM[address]
            hex_data:str = hex(int(data,2))[2:].zfill(4)
            f.write(f"{address}: {hex_data}\n")

writeROM(ROM_1_path, ROM_1)



    


        
    
