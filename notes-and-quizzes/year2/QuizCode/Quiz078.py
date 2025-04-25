#2023-09-18 Quiz 078
#Layer 4 Firewall

class firewall():
    def __init__(self, data:str):
        self.data = data

    def find_port(self):
        temp = 0
        power = 0
        for i in range(15,-1,-1):
            temp += int(self.data[i])*2**power
            power += 1
        return temp

    def layer4(self):
        print(f"Port: {self.find_port()}")
        if self.find_port()==80 or self.find_port()==22123:
            return "Allowed" , self.data[16:len(self.data)-1]
        return "Filtered", None

boi = firewall("100111001011001110010110011100101")
print(boi.layer4())

boi2 = firewall("010101100110101111110111001111")
print(boi2.layer4())