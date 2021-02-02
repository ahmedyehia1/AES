from AES import AES

cipher = AES()
ED = bool(int(input("Encrypt: 0, Decrypt: 1\n")))
key = input("Key: ")
text = input("Ciphertext: " if ED else "Plaintext: ")
print(cipher.Decrypt(text,key) if ED else cipher.Encrypt(text,key))