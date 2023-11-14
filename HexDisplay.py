class HexDisplay:
    def __init__(self):
        self.top = 0
        self.top_left = 0
        self.top_right = 0
        self.mid = 0
        self.bottom_left = 0
        self.bottom_right = 0
        self.bottom = 0
        self.dec = 0

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


    """
    Segments:
                    0 (top)
    1 (top left)                2 (top right)
                    3 (middle)
    4 (bottom left)             5 (bottom right)
                    6 (bottom)
                                7 (decimal point)"""

    def reset(self):
        self.top = 0
        self.top_left = 0
        self.top_right = 0
        self.mid = 0
        self.bottom_left = 0
        self.bottom_right = 0
        self.bottom = 0
        self.dec = 0

    def refresh(self):
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
        binary = ""
        for bit in self.bits:
            binary += str(bit)
        return binary
    
    def zero(self):
        self.reset()
        self.top = 1
        self.top_left = 1
        self.top_right = 1
        self.bottom_left = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def one(self):
        self.reset()
        self.top_right = 1
        self.bottom_right = 1
        return self.refresh()
    
    def two(self):
        self.reset()
        self.top = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_left = 1
        self.bottom = 1
        return self.refresh()
    
    def three(self):
        self.reset()
        self.top = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def four(self):
        self.reset()
        self.top_left = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_right = 1
        return self.refresh()
    
    def five(self):
        self.reset()
        self.top = 1
        self.top_left = 1
        self.mid = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def six(self):
        self.reset()
        self.top = 1
        self.top_left = 1
        self.mid = 1
        self.bottom_left = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def seven(self):
        self.reset()
        self.top = 1
        self.top_right = 1
        self.bottom_right = 1
        return self.refresh()
    
    def eight(self):
        self.reset()
        self.top = 1
        self.top_left = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_left = 1
        self.bottom_right = 1
        self.bottom = 1
        return self.refresh()
    
    def nine(self):
        self.reset()
        self.top = 1
        self.top_left = 1
        self.top_right = 1
        self.mid = 1
        self.bottom_right = 1
        return self.refresh()
    
    def getDigit(self,digit: str):
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
    
gen = HexDisplay()
ROM_1 = {}
for i in range(0,999):
    #convert i to a hex address of 4 digits
    address = hex(i)[2:].zfill(4)
    digits = [str(x) for x in str(i)]
    while len(digits) < 3:
        digits.insert(0,"0")
    #24 bit address
    digit_1 = gen.getDigit(digits[0])
    digit_2 = gen.getDigit(digits[1])
    digit_3 = gen.getDigit(digits[2])
    data = digit_1 + digit_2 + digit_3
    ROM_1[address] = data

#output path 
ROM_1_path = "hex_ROM_24bit"

def writeROM(path, ROM):
    with open(path, "w") as f:
        f.write("v3.0 hex words addressed\n")
        for address in ROM:
            data = ROM[address]
            hex_data = hex(int(data,2))[2:].zfill(4)
            f.write(f"{address}: {hex_data}\n")

writeROM(ROM_1_path, ROM_1)



    


        
    
