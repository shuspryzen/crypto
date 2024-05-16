def prepare_input(text):
    text = text.upper().replace(" ","").replace("J", "I")
    pairs = [text[i:i+2] for i in range(0, len(text), 2)]
    if len(pairs[-1]) == 1:
        pairs[-1] += "X"
    return pairs

def generate_key_square(key):
    key = key.upper().replace("J", "I")
    key_square = "".join(sorted(set(key), key=key.index))
    key_square += "".join(sorted(set("ABCDEFGHIKLMNOPQRSTUVWXYZ") - set(key_square)))
    return key_square

def find_position(key_square, letter):
    index = key_square.index(letter)
    return index // 5, index % 5

def encrypt(pair, key_square):
    row1, col1 = find_position(key_square, pair[0])
    row2, col2 = find_position(key_square, pair[1])
    if row1 == row2:
        return key_square[row1 * 5 + (col1 + 1) % 5] + key_square[row2 * 5 + (col2 + 1) % 5]
    elif col1 == col2:
        return key_square[((row1 + 1) % 5) * 5 + col1] + key_square[((row2 + 1) % 5) * 5 + col2]
    else:
        return key_square[row1 * 5 + col2] + key_square[row2 * 5 + col1]

def playfair_cipher(text, key):
    pairs = prepare_input(text)
    key_square = generate_key_square(key)
    return "".join(encrypt(pair, key_square) for pair in pairs)
plaintext = "Hide the gold in the tree stump"
key = "keyword"
cipher_text = playfair_cipher(plaintext, key)
print("Cipher Text:",cipher_text)
