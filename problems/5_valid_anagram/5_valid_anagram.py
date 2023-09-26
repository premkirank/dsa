import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def valid_anagram(str1, str2):
    str1_map = {}
    str2_map = {}
    
    if len(str1) != len(str2):
        return False
    
    for letter in str1:
        if letter in str1_map:
            str1_map[letter] += 1
        else:
            str1_map[letter] = 1
            
    for letter in str2:
        if letter in str2_map:
            str2_map[letter] += 1
        else:
            str2_map[letter] = 1

    for key in str1_map:
        try:
            if str1_map[key] != str2_map[key]:
                return False
        except Exception as _:
            return False

    return True


if __name__ == "__main__":
    str1 = "anagram"
    str2 = "nagaram"
    
    str1 = "aa"
    str2 = "bb"
    
    str1 = "a"
    str2 = "ab"

    validity = valid_anagram(str1, str2)
    print(validity)
