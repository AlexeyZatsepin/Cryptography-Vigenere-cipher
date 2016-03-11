#!/usr/bin python
# -*- coding: utf-8 -*-
import re
from math import log
import itertools


def create_letter_dict_from_text(filename):
    with open(filename, 'r') as cursor:
        cipher = cursor.read()
        words = cipher.lower().split()
        dictionary = dict()
        for word in words:
            for letter in word:
                if re.match(r'[a-zа-я]+$', letter) is not None:
                    dictionary[letter] = dictionary.get(letter, 0) + 1
        print (dictionary)
        return dictionary


def create_bigram_dict_from_file(filename, dictionary):
    bigrams = {}.fromkeys(map(''.join, itertools.product(dictionary, repeat=2)), 0)
    with open(filename, 'r') as cursor:
        text = cursor.read()
        for key in range(1, len(text)):
            bigram = text[key - 1] + text[key]
            if bigram in bigrams:
                bigrams[bigram] += 1
    ideal_bigrams={}
    for bigram in bigrams:
        if bigrams[bigram] != 0:
            ideal_bigrams[bigram]=bigrams[bigram]
    return ideal_bigrams


def frequency_analytics(dictionary):
    frequency = zip(dictionary.keys(), map(lambda x: float(x) / sum(dictionary.values()), dictionary.values()))
    return frequency


def set_txt_in_csv(filename, result):
    with open(filename, 'w') as cursor:
        cursor.write('\n'.join('%s : %s' % line for line in result))


def entropy(frequency, n):
    H = 0
    for letter in frequency:
        if letter[1] != 0:
            H += -(letter[1] * log(letter[1], 2))
    return H / int(n)


if __name__ == '__main__':
    dictionary = create_letter_dict_from_text('plain_texts/yogurt_eng.txt')
    bigrams = create_bigram_dict_from_file('plain_texts/yogurt_eng.txt', dictionary)
    letter_result = frequency_analytics(dictionary)
    bigrams_result=frequency_analytics(bigrams)
    set_txt_in_csv('results/yogurt_letters.csv', letter_result)
    set_txt_in_csv('results/yogurt_bigram.csv', bigrams_result)
    n = input("Enter n:\n")
    print (entropy(letter_result, n))
    print (entropy(bigrams_result,n))
