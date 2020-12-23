import nltk
nltk.download('words')

english_words = nltk.corpus.words.words()

# all_letters =list(map(chr, range(97, 123)))
# ALPHABET = ''.join(all_letters).upper() #ABCDEFGHIJKLMNOPQRSTUVWXYZ


def encrypt(text,key):
    encrypted = ''
    for char in text:
        if char.isalpha() == True:
            if char == char.lower():
                pos = ord(char) - 97
                pos += key
                pos = pos % 26 # loop agai
                encrypted += chr(pos +  97)
            else:
                pos = ord(char) - 65
                pos += key
                pos = pos % 26 # loop agai
                encrypted += chr(pos +  65)
        else:
            encrypted += char
    return encrypted

def decrypt(text,key):
    return encrypt(text,-1*key)

def find_key (encrypted):
    results = {}
    for i in range(26):
        sentence = decrypt(encrypted,i)
        matched = 0
        sentence_words = sentence.split()
        for word in sentence_words:
            if word in english_words:
                matched += 1
        results[f'{i}'] = matched
    max_key = max(results, key=results.get)
    return int(max_key)


if __name__ == "__main__":
    # all_letters =list(map(chr, range(97, 123)))
    # st = ''.join(all_letters)

    encrypted = encrypt('I love python',7)
    print(encrypted)

    print(find_key(encrypted))

    decrypted = decrypt(encrypted,7)
    print(decrypted)