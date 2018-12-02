import base64
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto import Random
from binascii import unhexlify
from binascii import hexlify

def encrypt(key, source, encode=True):
    source = unhexlify(source)  
    key = unhexlify(key)
    IV = Random.new().read(16)  # Gera IV
    encryptor = AES.new(key, AES.MODE_CBC, IV) #Encripta
    padding = AES.block_size - len(source) % AES.block_size  # Calcula PAD
    source += bytes([padding]) * padding  # Padding
    data = IV + encryptor.encrypt(source)# IV + Cifra
    return  bytes.decode(hexlify(data))

msg = encrypt("140b41b22a29beb4061bda66b6747e14","4e657874205468757273646179206f6e65206f66207468652062657374207465616d7320696e2074686520776f726c642077696c6c2066616365206120626967206368616c6c656e676520696e20746865204c696265727461646f72657320646120416d6572696361204368616d70696f6e736869702e")
print("Texto Claro:",bytes.decode(unhexlify("4e657874205468757273646179206f6e65206f66207468652062657374207465616d7320696e2074686520776f726c642077696c6c2066616365206120626967206368616c6c656e676520696e20746865204c696265727461646f72657320646120416d6572696361204368616d70696f6e736869702e"))
,"\nMensagem Cifrada --->",msg)