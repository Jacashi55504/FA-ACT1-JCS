# Intercambio de claves
# JCS

import hashlib
import random

# Numero primo de RFC3526 de 1536 bits - MODFP Group

p = int ("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA237327FFFFFFFFFFFFFFFF", 16)
g = 2

print("\n", "**********************************")
print("\n", "        Variables publicas        ")
print("\n", "**********************************")
print("\n", "Numero privado compartido: " , p)
print("\n", "Numero publico compartido: " , g)

# Random, mensaje publico

sAlice = random.getrandbits(256)
sBob = random.getrandbits(256)

print("\n", "Numero de alice: " , sAlice)
print("\n", "Numero de bob: " , sBob)

A = pow(g, sAlice, p)
B = pow(g, sBob, p)

print("\n", "Mensaje de Alice a Bob: " , A)
print("\n", "Mensaje de Bob a Alice: " , B)

# Alice calcula la llave secreta compartida

s1 = pow(B, sAlice, p)
s2 = pow(A, sBob, p)


print("\n", "Llave secreta compartida: " , s1)