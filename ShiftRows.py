import numpy as np

def ShiftRows(plaintext,inv=False):
    for i,r in enumerate(plaintext):
        plaintext[i] = np.roll(r,i if inv else -i)
    return plaintext