#! python3
# Wordscapes Cheat - to view all possible answers by entering all available letters

import json
import time
from itertools import combinations
from itertools import permutations


def load_words():
    try:
        with open('word_dictionary.json', 'r') as dictionary:
            return json.load(dictionary)
    except Exception as e:
        return str(e)


def get_word_length(n):
    word_list = []
    for word_combination in list(combinations(available_letters, i)):
        for word in list(permutations(word_combination)):
            word = ''.join(word)
            if english_words.get(word):
                if word not in word_list:
                    word_list.append(word)
    return word_list


def sort_print_words(words):
    words.sort()
    for w in words:
        print(w)


print('Enter available letters: ', end='')
available_letters = list(input())
print('Enter Desired Word Length')
print('(0 or greater than or equal to the length of available letters shows all valid words): ', end='')
word_length = int(input())

start_time = time.time()
english_words = load_words()

if word_length > 0 or word_length <= len(available_letters):
    for i in range(3, len(available_letters) + 1):
        print('=' * 20)
        print(f'Word Length {i}:')
        sort_print_words(get_word_length(i))

else:
    sort_print_words(get_word_length(word_length))

print('')
print(f'Program Finished at {time.time() - start_time:.4f}s')