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


print('Enter available letters: ', end='')
english_words = load_words()
available_letters = list(input())
start_time = time.time()


for i in range(3, len(available_letters) + 1):
    print('=' * 20)
    print(f'Word Length {i}:')
    word_list = []
    for word_combination in list(combinations(available_letters, i)):
        for word in list(permutations(word_combination)):
            word = ''.join(word)
            if english_words.get(word):
                word_list.append(word)
    word_list.sort()
    for word in word_list:
        print(word)

print(f'Program Finished at {time.time() - start_time:.4f}s')