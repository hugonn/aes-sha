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
    cifra = unhexlify(cifra)    #Transforma em bytes a informação que está hexa
    chave = unhexlify(chave)    #Transforma em bytes a informação que está hexa
    IV = cifra[:16]             #Recupera o IV dos 16 primeiros bytes
    aes_obj = AES.new(chave, AES.MODE_CBC, IV) #Utiliza função do PyCrypto
    texto = aes_obj.decrypt(cifra[16:]) #Decripta a mensagem sem o IV
    padding = texto[-1]                 #Retira o pad
    return bytes.decode(texto[:-padding]) #Decodifica os Bytes

key = "140b41b22a29beb4061bda66b6747e14"
msg_cifrada2 = "4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81"
msg_cifrada1 = "45a68b1314cde15d06f8adb75f070feba3e08131f0c9d17a1ceb5bc068c30dea150f2a24014cf70e6ba760ccd110d56a49c3d487911b211929f47e2f94e3688d400f5b88e249240b5683579910ceb3b4536004834f65255b4da8cb44ba7e10b74ec464ac8a71971175811a8b50efb744db8cef0771e6ad9e4b5b9cb22c4d40896a1215e15ffaf0c1ba08c978212928f6"
msg = decriptar_hex(msg_cifrada2,key) 
msg2 = decriptar_hex(msg_cifrada1,key)
print("\n",msg,"\n")
print(msg2,"\n") 

