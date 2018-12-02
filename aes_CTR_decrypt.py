import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import unhexlify
from binascii import hexlify

def int_of_string(s):
    return int(binascii.hexlify(s), 16) #contador aleatorio por conta do CTR


def decrypt_CTR(key, cifra):
    cifra = unhexlify(cifra)    #Transforma em bytes a informação que está hexa
    key = unhexlify(key)        #Transforma em bytes a informação que está hexa
    iv = cifra[:16]             #Cria o "bloco falso"    
    ctr = Counter.new(128, initial_value=int_of_string(iv)) #Cria objeto AES em modo CTR
    aes = AES.new(key, AES.MODE_CTR, counter=ctr) # Decripta cifra
    return bytes.decode(aes.decrypt(cifra[16:]))  # Retorna o texto claro decodificado


msg_cifrada = "69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329"
msg_cifrada2 ="770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451"
key = "36f18357be4dbd77f050515c73fcf9f2"
msg_clara = decrypt_CTR(key,msg_cifrada)
msg_clara2 = decrypt_CTR(key,msg_cifrada2)
print("Mensagem Encriptada ----->",msg_cifrada,"\nMensagem Clara ------>",msg_clara)
print("\nMensagem Encriptada ----->",msg_cifrada2,"\nMensagem Clara ------>",msg_clara2)