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
        roundCount = 9
        roundKey = np.array([int(key[i:i+2],16) for i in range(0,len(key),2)]).reshape(4,4).T
        ciphertext = np.array([int(ciphertext[i:i+2],16) for i in range(0,len(ciphertext),2)]).reshape(4,4).T

        ciphertext = ciphertext ^ roundKey
        ciphertext = ShiftRows(ciphertext,inv=True)
        ciphertext = Sbox(ciphertext,inv=True)
        for r in range(roundCount):
            roundKey = KeyGen(roundKey,roundCount-r,inv=True)
            ciphertext = ciphertext ^ roundKey
            ciphertext = MixColumns(ciphertext,inv=True)
            ciphertext = ShiftRows(ciphertext,inv=True)
            ciphertext = Sbox(ciphertext,inv=True)
        roundKey = KeyGen(roundKey,0,inv=True)
        ciphertext = ciphertext ^ roundKey
        return "".join([("" if x > 15 else "0") + hex(x)[2:] for x in ciphertext.T.ravel()])

A = AES()
plaintext = "0123456789ABCDEF0123456789ABCDEF"
key       = "0123456789ABCDEF0123456789ABCDEF"
invKey    = "8821df9e5e9a36f31255d04529bedb5e"
print(f"plaintext: {plaintext}")
e = A.Encrypt(plaintext,key)
print(f"encrypted: {e}")
d = A.Decrypt(e,invKey)
print(f"decrypted: {d}")