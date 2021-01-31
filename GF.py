import numpy as np

class GF:
    def __init__(self,val):
        self.val = val

    def __add__(self,gf):
        return GF(self.val ^ gf.val)

    def __mul__(self,gf):
        a = self.val
        b = gf.val
        imd = 0
        while a > 0:
            imd ^= b*(a%2)
            a,b = a//2,2*b
        return self.remainder(imd)

    def remainder(self,imd):
        irreducible = 283 # x^8 + x^4 + x^3 + x + 1
        digits = []
        while np.log2(imd) > 9:
            digits.insert(0,imd%2)
            imd = imd//2
        while True:
            while np.log2(imd) < 8:
                if len(digits) == 0: return GF(imd)
                imd = 2*imd + digits[0]
                digits.pop(0)
            imd = irreducible ^ imd
   
# print(~GF(4))
# print((GF(0xd4)*GF(2) + GF(0xbf)*GF(3) + GF(0x5d)*GF(1) + GF(0x30)*GF(1)).val)