import numpy as np
from Sbox import Sbox
from ShiftRows import ShiftRows
from MixColumns import MixColumns
from KeyGen import KeyGen

class AES:
    def Encrypt(self,plaintext,key):
        roundCount = 10
        roundKey = np.array([int(key[i:i+2],16) for i in range(0,len(key),2)]).reshape(4,4).T
        plaintext = np.array([int(plaintext[i:i+2],16) for i in range(0,len(plaintext),2)]).reshape(4,4).T
        plaintext = plaintext ^ roundKey
        for r in range(roundCount):
            plaintext = Sbox(plaintext)
            plaintext = ShiftRows(plaintext)
            plaintext = MixColumns(plaintext,final=not bool(roundCount-r-1))
            roundKey = KeyGen(roundKey,r)
            plaintext = plaintext ^ roundKey
        return "".join([("" if x > 15 else "0") + hex(x)[2:] for x in plaintext.T.ravel()])
    def Decrypt(self,ciphertext,key):
        pass

A = AES()
print(A.Encrypt("0189fe7623abdc5445cdba3267ef9810","0f470caf15d9b77f71e8ad67c959d698"))