
from math import gcd

def isCoprime(N,phi,n):
    if (gcd(N,n) and gcd(phi,n)) == 1:
        return True
    else: 
      return False


p = 541
q = 643
N = p * q
phi = (p-1) * (q-1)
e = 0
#1 < e < phi(N)
#coprime with (N, phi(N))
for i in range(2,phi):
    if isCoprime(N,phi,i):
        e = i
print("--->Coprime(N, phi(N) =", e)


#choose d: d*e mod(phi(N))

d = 0
counter = 0
position = 1
maxVal = e*phi
while d==0:
    counter += e
    if(counter % phi == 1 and counter > maxVal):
        d = position
    position += 1

public_key_pair = [e,q] #key
private_key_pair = [d,q] #padlock

print("Public key pair", public_key_pair)
print("Private key pair", private_key_pair)


msg = 'This is a message for Gustavo Mendez'
msg_numbers = []
for letter in msg:  
  msg_numbers.append(ord(letter))

msg_encrypted = []

for l_number in msg_numbers:
  msg_encrypted.append(l_number ** public_key_pair[0] % public_key_pair[1])


encrypted = ""
for l_num_encrypted in msg_encrypted:
  encrypted += chr(l_num_encrypted)
print("\nMessage encrypted" , encrypted)

#decryption
dec_msg = []
for enc_num_letter in msg_encrypted:
  dec_msg.append(enc_num_letter ** private_key_pair[0] % public_key_pair[1])

#print decrypted message
decrypted = ""
for dec_letter in dec_msg:
  decrypted += chr(dec_letter)
print("\n Message decrypted", decrypted)