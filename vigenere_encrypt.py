# coding=utf-8
import re
from index_maching import index_maching


def key(length, keyword):
    if length > len(keyword):
        while length > len(keyword):
            keyword += keyword[:length - len(keyword)]
        return keyword
    else:
        return keyword[:length]


def create_alphabet(language):
    if language == 'eng':
        alphabet = {chr(i): i - 97 for i in range(97, 123)}
    else:
        rus = u'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        alphabet = {rus[i]: i for i in range(len(rus))}
    return alphabet


def encipher(word, alphabet, key):
    temp_list = list()
    substitution_alphabet = {value: key for key, value in alphabet.items()}
    for i in range(len(word)):
        if word[i] not in alphabet.keys():
            temp_list.append(word[i])
        else:
            temp_list.append(substitution_alphabet[(alphabet[word[i]] + alphabet[key[i]]) % len(alphabet)])
    cipher = ''.join(temp_list)
    return cipher


def encode_file(filename,keyword):
    with open('plain_texts/%s.txt' % filename, 'r') as cursor:
        plain_text = cursor.read().lower()
        plain_text = re.sub(r'[^a-zа-я]', '', plain_text)
        print ("Plain text index maching: " + str(index_maching(plain_text)))
    if 'eng' in filename:
        alphabet = create_alphabet('eng')
    else:
        alphabet = create_alphabet('ru')
    uniqe_key = key(len(plain_text), keyword)
    cipher = encipher(plain_text, alphabet, uniqe_key)
    with open('ciphers/%s_%s.txt' % (filename, keyword), 'w') as cursor:
        cursor.write(cipher)
        print ("Cipher text index maching: " + str(index_maching(cipher)))


def encode_text(plain_text,keyword,alph):
    uniqe_key = key(len(plain_text), keyword)
    cipher = encipher(plain_text, alph, uniqe_key)
    return cipher


if __name__ == '__main__':
    global filename
    while True:
        try:
            filename = input("Enter filename:\n")
            keyword = input("Enter keyword for encoding %s:\n" % filename)
            keyword = keyword.lower()
            break
        except:
            print ("Try again")
    encode_file(filename,keyword)
    # global word, keyword
    # while True:
    #    try:
    #        word = input("Enter word:\n")
    #        keyword = input("Enter key:\n")
    #        word = word.lower()
    #        word = re.sub(r'\s', '', word)
    #        keyword = keyword.lower()
    #        break
    #    except:
    #        print "Try again"
    # alphabet = create_alphabet()
    # key = key(len(word), keyword)
    # print 'word:' + word
    # print 'key:' + key
    # cipher = encipher(word, alphabet, key)
    # print 'cipher:' + cipher
