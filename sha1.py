import hashlib
def calc_sha1(text):
    sha1_hash=hashlib.sha1(text.encode()).hexdigest()
    return sha1_hash

text = "Hello There!"
print(text)
print(calc_sha1(text))