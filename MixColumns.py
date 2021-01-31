import numpy as np
from GF import GF

def MixColumns(plaintext,inv=False,final=False):
    if final: return plaintext
    matrix = [
    np.vectorize(GF)(np.array([
        [2,3,1,1],
        [1,2,3,1],
        [1,1,2,3],
        [3,1,1,2],
    ])),
    np.vectorize(GF)(np.array([
        [14,11,13,9],
        [9,14,11,13],
        [13,9,14,11],
        [11,13,9,14],
    ]))]
    plaintext = np.vectorize(GF)(plaintext)
    return np.vectorize(lambda x: x.val)(np.dot(matrix[inv],plaintext))
