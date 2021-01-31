import numpy as np
from Sbox import Sbox

def KeyGen(roundKey,i):
    Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
    # Rcon vector
    RC = np.pad(np.array([[Rcon[i]]]),[(0,3),(0,0)])
    roundKey[:,0] = roundKey[:,0].ravel() ^ RC.ravel() ^ Sbox(np.roll(roundKey[:,3],-1,axis=0))
    roundKey[:,1] = roundKey[:,1].ravel() ^ roundKey[:,0].ravel()
    roundKey[:,2] = roundKey[:,2].ravel() ^ roundKey[:,1].ravel()
    roundKey[:,3] = roundKey[:,3].ravel() ^ roundKey[:,2].ravel()
    return roundKey