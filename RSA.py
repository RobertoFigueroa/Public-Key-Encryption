from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

keyPair = RSA.generate(3072)

pubKey = keyPair.publickey()
print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

# Message 
msg = b'This is a message for Roberto Figueroa'
encrypted = PKCS1_OAEP.new(pubKey).encrypt(msg)
print("Encrypted:", binascii.hexlify(encrypted))

decrypted = PKCS1_OAEP.new(keyPair).decrypt(encrypted)
print('Decrypted:', decrypted)