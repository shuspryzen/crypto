import hashlib
def calc_sah1(text):
    md5_hash=hashlib.md5(text.encode()).hexdigest()
    return md5_hash

text = "Hello There!"
print(text)
print(calc_sah1(text))