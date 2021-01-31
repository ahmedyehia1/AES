import numpy as np
from Sbox import Sbox
from ShiftRows import ShiftRows
from MixColumns import MixColumns
from KeyGen import KeyGen

class AES:
    def Encrypt(self,plaintext,key):
        roundCount = 10
        roundKey = key
        plaintext = np.array([int(plaintext[i:i+2],16) for i in range(0,len(plaintext),2)]).reshape(4,4)
        for r in range(roundCount):
            plaintext = Sbox(plaintext)
            plaintext = ShiftRows(plaintext)
            plaintext = MixColumns(plaintext,final=not bool(roundCount-r-1))
            plaintext = plaintext ^ roundKey
            roundKey = KeyGen(roundKey)
            pass
    def Decrypt(self,ciphertext,key):
        pass
