import sys
import os
from functools import reduce
from operator import itemgetter

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def group_anagrams(strs):
    anagrams_map = {}
    
    for str in strs:
        str_distribution_map = {}
        for letter in str:
            if letter in str_distribution_map:
                str_distribution_map[letter] += 1
            else:
                str_distribution_map[letter] = 1
        
        if len(anagrams_map) == 0:
            anagrams_map[str] = str_distribution_map
            # print(str, anagrams_map)
            continue

        for anagrams_str, existing_distribution_map in anagrams_map.items():
            anagram_match_found = True

            min_anagram = anagrams_str.split(",")
            if len(min_anagram[0]) != len(str):
                anagram_match_found = False
                continue
            
            for letter, count in str_distribution_map.items():
                if letter not in existing_distribution_map or count != existing_distribution_map[letter]:
                    anagram_match_found = False
                    continue
                                
            if anagram_match_found:
                anagram_group = "%s,%s" % (anagrams_str, str)
                anagrams_map[anagram_group] = existing_distribution_map
                del anagrams_map[anagrams_str]
                break

        if not anagram_match_found:
            anagrams_map[str] = str_distribution_map

        # print(str, anagrams_map)

    return [anagram_group.split(",") for anagram_group in anagrams_map]

@timeit
def group_anagrams_map(strs):
    anagrams_map = {}

    for string in strs:
        str_letter_sequence_count = [0] * 26
        for letter in string:
            str_letter_sequence_count[ord(letter) - 97] += 1

        if str(str_letter_sequence_count) in anagrams_map:
            anagrams_map[str(str_letter_sequence_count)].append(string)
        else:
            anagrams_map[str(str_letter_sequence_count)] = [string]

    return list(anagrams_map.values())


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat", "good", "dogo"]
    strs = ["ddddddddddg", "dgggggggggg"]
    
    output = group_anagrams(strs)
    print(output)
    
    output = group_anagrams_map(strs)
    print(output)