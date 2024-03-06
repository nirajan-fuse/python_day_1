# Given an array of strings (str), group the anagrams together. You can return the answer in any order.

from collections import defaultdict

def group_anagrams(strings):
    anagrams_map = defaultdict(list)

    for string in strings:
        sorted_string = ''.join(sorted(string))
        
        anagrams_map[sorted_string].append(string)
    
    return anagrams_map.values()

strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(strs))

