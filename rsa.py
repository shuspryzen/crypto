import random
def gcd(a,b):
    while b!=0:
        a,b = b,a % b
    return a

def mod_inverse(a,m):
    m0,x0,x1 = m,0,1
    while a>1:
        q = a//m
        m,a = a%m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p,q):
    n = p*q
    phi = (p-1) * (q-1)
    e = random.randrange(1,phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randrange(1,phi)
        g = gcd(e,phi)
    d = mod_inverse(e,phi)
    return ((e,n),(d,n))

def encrypt(pubkey,plain):
    key,n = pubkey
    cipher_text = [pow(ord(char), key, n) for char in plain]
    return cipher_text

def decrypt(private_key,cipher_text):
    key,n = private_key
    plain_text = [chr(pow(char,key,n)) for char in cipher_text]
    return ''.join(plain_text)

def main():
    p=61
    q=53
    public_key,private_key = generate_keypair(p,q)
    print("Public: ",public_key)
    print("Private: ",private_key)
    message = "Hello,RSA!"
    enc= encrypt(public_key,message)
    print(enc)
    dec= decrypt(private_key,enc)
    print(dec)

if __name__ == "__main__":
    main()