from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Crypto import Random
from Crypto.Cipher import AES
from binascii import unhexlify
from binascii import hexlify
from base64 import b16encode
from Crypto.Hash import SHA256

#Arquivo que contem o decriptador AES_hex    
def decriptar_hex(cifra,chave):
    cifra = unhexlify(cifra)    #Transforma em bytes a info em hexa
    chave = unhexlify(chave)    #Transforma em bytes a info em hexa
    IV = cifra[:16]             #Recupera o IV dos 16 primeiros bytes
    aes_obj = AES.new(chave, AES.MODE_CBC, IV) #Utiliza função do PyCrypto
    texto = aes_obj.decrypt(cifra[16:]) #Decripta a mensagem sem o IV
    padding = texto[-1]                 #Retira o pad
    return bytes.decode(texto[:-padding]) #Decodifica os Bytes

key = "140b41b22a29beb4061bda66b6747e14"
msg_cifrada2 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
msg_cifrada1 = "5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253"
msg = decriptar_hex(msg_cifrada1,key) 
msg2 = decriptar_hex(msg_cifrada2,key)
print("\n",msg,"\n")
print(msg2,"\n") 

