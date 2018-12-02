import binascii
import os
from Crypto.Cipher import AES
from Crypto.Util import Counter
from binascii import unhexlify
from binascii import hexlify
from Crypto import Random

def int_of_string(s):
    return int(binascii.hexlify(s), 16) # Contador aleatorio por conta do CTR

def encrypt_CTR(key, texto):
    texto = unhexlify(texto) #Transforma em bytes a informação que está hexa
    key = unhexlify(key)     #Transforma em bytes a informação que está hexa
    iv = Random.new().read(16)     #Cria o "bloco falso"
    ctr = Counter.new(128, initial_value=int_of_string(iv)) #cria objeto que encripta no modo CTR
    aes = AES.new(key, AES.MODE_CTR, counter=ctr) #encripta cifra
    return bytes.decode(hexlify(iv + aes.encrypt(texto)))  # Retorna cifra encriptada


msg_clara = "CTR mode lets you build a stream cipher from a block cipher"
msg_clara2 = "5468697320697320612073656e74656e636520746f20626520656e63727970746564207573696e672041455320616e6420435452206d6f64652e"
key = "36f18357be4dbd77f050515c73fcf9f2"

msg_encriptada= encrypt_CTR(key,hexlify(str.encode(msg_clara)))
msg_encriptada2 = encrypt_CTR(key,msg_clara2)

print("Mensagem Clara ----->",msg_clara,"\nMensagem Encriptada ------>",(msg_encriptada))
print("\nMensagem Clara ----->",bytes.decode(unhexlify(msg_clara2)),"\nMensagem Encriptada ------>",(msg_encriptada2))