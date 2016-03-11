# coding=utf-8
import re


def index_maching(text):
    words = text.lower()
    dictionary = {}
    result = 0
    for word in words:
        for letter in word:
            if re.match(r'[а-я]+$', letter) is not None:
                dictionary[letter] = dictionary.get(letter, 0) + 1
    for key, value in dictionary.items():
        result += value * (value - 1)
    result = float(result) / (len(text) * (len(text) - 1))
    return result

if __name__=='__main__':
    with open('ciphers/variant6.txt') as cursor:
    #with open('plain_texts/просто.txt') as cursor:
        text = cursor.read()
        print (index_maching(text))