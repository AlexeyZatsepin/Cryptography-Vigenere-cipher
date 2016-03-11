# coding=utf-8
import re
from index_maching import index_maching
from vigenere_encrypt import create_alphabet, key ,encode_text
from entropy_frequency import frequency_analytics


def decipher(cipher, alphabet, keyword):
    temp_list = list()
    substitution_alphabet = {value: key for key, value in alphabet.items()}
    for i in range(len(cipher)):
        if cipher[i] not in alphabet.keys():
            temp_list.append(cipher[i])
        else:
            temp_list.append(substitution_alphabet[(alphabet[cipher[i]] - alphabet[keyword[i]]) % len(alphabet)])
    word = ''.join(temp_list)
    return word


def key_length_finder(text, standard_index):
    index_list = list()
    temp_list=list()
    for i in range(20):
        #for j in range(i+1):
            #temp_list.append(index_maching(text[j::i + 1]))
            #print(index_maching(text[j::i+1]))
        #average=sum(temp_list)/len(temp_list)
        #index_list.append(average)
        index_list.append(index_maching(text[::i+1]))
        #print(str(i+1)+': '+str(index_list[i]))
    print(index_list)
    index_list = [abs(1 / (standard_index - x)) for x in index_list]
    print(index_list)
    length = index_list.index(max(index_list)) + 1
    return length


def key_breaker(length, alphabet, cipher_text, standart_letter):
    global most_common_letter
    substitution_alphabet = {value: key for key, value in alphabet.items()}
    dictionary = dict()
    k = ''
    for i in range(length):
        for letter in cipher_text[i::length]:
            if re.match(r'[а-яa-z]+$', letter) is not None:
                dictionary[letter] = dictionary.get(letter, 0) + 1
        #print (dictionary)
        for letter, count in dictionary.items():
            if count == max(dictionary.values()):
                most_common_letter = letter
                #print(most_common_letter)
        k += substitution_alphabet[(alphabet[most_common_letter] - alphabet[standart_letter]) % len(alphabet)]
        dictionary.clear()
    print(k)
    return k


def second_lenght_finder(text,standart_index,alph):
    with open('plain_texts/common_russian.txt') as cursor:
        common_text=cursor.read()
        cipher_index=index_maching(text)
        print(cipher_index)
        temp_list=list()
        pswd='вовчерашнемматчепобедил'#анаилучшаякоманда'
        for i in range(len(pswd)):
            temp_list.append(index_maching(encode_text(common_text,pswd[i:],alph)))
            print (i)
        index_list = [abs(1 / (cipher_index - x)) for x in temp_list]
        print(index_list)
        length = index_list.index(max(index_list)) + 1
        print (length)


if __name__ == '__main__':
    #try:
    filename = input("Enter cipher text filename:\n")
    with open('ciphers/%s.txt' % filename) as cursor:
        if 'eng' in filename:
            alph = create_alphabet('eng')
            standard_index = 0.0644
            standart_letter = 'e'
        else:
            alph = create_alphabet('ru')
            standard_index = 0.0553
            standart_letter = 'о'
        cipher = cursor.read()
        #cipher = re.sub(r'[^a-zа-я]','', cipher_with_trash)
        length = key_length_finder(cipher, standard_index)
        #second_lenght_finder(cipher,standard_index,alph)
        print (length)
        k = key_breaker(length, alph, cipher, standart_letter)
        keyword = key(len(cipher), k)
        print(u'возвращениеджинна')
        keyword = key(len(cipher), u'возвращениеджинна')
        print (decipher(cipher, alph, keyword))
    #except:
        #    print ("File not found")
