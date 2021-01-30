import numpy as np

class GF:
    def __init__(self,val):
        self.val = val
    def __add__(self,gf):
        return self.val ^ gf.val
    def __mul__(self,gf):
        a = self.val
        b = gf.val
        imd = 0
        while a > 0:
            imd ^= b*(a%2)
            a,b = int(a/2),2*b
        irreducible = 155 # x^8 + x^4 + x^3 + x + 1
        digits = []
        while np.log2(imd) > 8:
            digits.insert(0,imd%2)
            imd = int(imd/2)
        while True:
            while np.log2(imd) < 7:
                if len(digits) == 0: return imd
                imd = 2*imd + digits[0]
                digits.pop(0)
            imd = irreducible ^ imd
