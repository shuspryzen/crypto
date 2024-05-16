from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode, b64encode

def des_enc(key,plain):
    cipher  = DES.new(key,DES.MODE_ECB)
    padded = pad(plain,32)
    encrypted = cipher.encrypt(padded)
    return b64encode(encrypted)

def des_dec(key,encrypted):
    cipher  = DES.new(key,DES.MODE_ECB)
    decrypted = cipher.decrypt(b64decode(encrypted))
    unpaddded = unpad(decrypted,32)
    return unpaddded

def main():
    plain = b"Hello,DES!"
    key = get_random_bytes(8)
    encrypted = des_enc(key,plain)
    print("Encrypted : "+ encrypted.decode())
    decrypted = des_dec(key, encrypted)
    print("Decrypted : "+ decrypted.decode())

if __name__ == "__main__":
    main()