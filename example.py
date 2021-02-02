from AES import AES

A = AES()
plaintext = "0123456789ABCDEF0123456789ABCDEF"
key       = "0123456789ABCDEF0123456789ABCDEF"
print(f"plaintext: {plaintext}")
e = A.Encrypt(plaintext,key)
print(f"encrypted: {e}")
d = A.Decrypt(e,key)
print(f"decrypted: {d}")