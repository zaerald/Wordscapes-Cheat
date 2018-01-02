#! python3
# Wordscapes Cheat - to view all possible answers by entering all available letters

import json
import os
import sys
import time
from itertools import permutations


print('Enter available letters: ', end='')
available_letters = list(input())
start_time = time.time()

for word in list(permutations(available_letters)):
    word = ''.join(word)
    print(word)


print(f'Program Finished at {time.time() - start_time:.4f}s')