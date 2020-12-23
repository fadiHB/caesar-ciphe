import nltk
nltk.download('words')

all_letters =list(map(chr, range(97, 123)))
ALPHABET = ''.join(all_letters).upper() #ABCDEFGHIJKLMNOPQRSTUVWXYZ


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


if __name__ == "__main__":
    all_letters =list(map(chr, range(97, 123)))
    st = ''.join(all_letters)

    encrypted = encrypt('abcd yz',2)
    print(encrypted)

    decrypted = decrypt(encrypted,2)
    print(decrypted)
  
    # print(ord('a'))
    # print(ord('A'))
    # print(1%26)


    # print('*'*30)
    # print('} = ' ,ord('}'))
    # print('{ = ' ,ord('{'))
    # print('*'*30)
    # # print(20%1)
