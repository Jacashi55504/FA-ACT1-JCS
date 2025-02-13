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

# Random, claves privadas entre Eve, Alice y Bob
sEve = random.getrandbits(256)
sAlice = random.getrandbits(256)
sBob = random.getrandbits(256)

print("\n", "Numero de alice: " , sAlice)
print("\n", "Numero de bob: " , sBob)
print("\n", "Número de Eve: ", sEve)



# Eve genera valores 
A = pow(g, sAlice, p)
EA = pow(g, sEve, p)
print("\n", f'Mensaje de Alice a Bob: {A}')

# Bob manda mensaje a Alice pero Eve lo intercepta
B = pow(g, sBob, p)
EB = pow(g, sEve, p)
print("\n", f'Mensaje de Bob a Alice: {B}')

# Alice y Bob calculan su llave secreta con el valor de Eve
K_Alice_Eve = pow(EB, sAlice, p)  
K_Bob_Eve = pow(EA, sBob, p)

#Eve conoce las laves compartidas
K_Eve_Alice = pow(A, sEve, p)
K_Eve_Bob = pow(B, sEve, p)

if K_Alice_Eve == K_Bob_Eve:
    print("\n✅ MITM exitoso: Eve obtuvo la clave secreta de Alice y Bob.")

hash_key_AE = hashlib.sha256(str(K_Alice_Eve).encode()).hexdigest()
hash_key_BE = hashlib.sha256(str(K_Bob_Eve).encode()).hexdigest()
print("\n Hash de la llave compartida:", hash_key_AE)
print("\n Hash de la llave compartida:", hash_key_BE)


