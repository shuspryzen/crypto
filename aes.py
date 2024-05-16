from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from base64 import b64decode, b64encode

def aes_enc(key,plain):
    cipher  = AES.new(key,AES.MODE_ECB)
    padded = pad(plain,32)
    encrypted = cipher.encrypt(padded)
    return b64encode(encrypted)

def aes_dec(key,encrypted):
    cipher  = AES.new(key,AES.MODE_ECB)
    decrypted = cipher.decrypt(b64decode(encrypted))
    unpaddded = unpad(decrypted,32)
    return unpaddded

def main():
    plain = b"Hello,AES!"
    key = get_random_bytes(16)
    encrypted = aes_enc(key,plain)
    print("Encrypted : "+ encrypted.decode())
    decrypted = aes_dec(key, encrypted)
    print("Decrypted : "+ decrypted.decode())

if __name__ == "__main__":
    main()