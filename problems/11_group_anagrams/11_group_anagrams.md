# Problem

https://leetcode.com/problems/group-anagrams/

# Companies

# Level

Medium

# Status

All tests passed but was not optimal approach

# Tags

Arrays, Hash Table, Strings, Sorting

# Approaches

- Map Approach
  - For each string, if not present in map add as key and maintain a map of letters against count as value
  - Check new string against existing map values, if match is there delete old key and create new key of both pairs with same value
  - Return list of all keys as lists
- Better Map Approach
  - Maintain a map to store sequence of 26 character string sequence counts as key
  - For each string, if not present in map add this string as key
  - Check new string against existing map values, if match is there append string to that list
  - Return list of all map values

# Resources

- https://leetcode.com/problems/group-anagrams/solutions/2384037/python-easily-understood-hash-table-fast-simple/
- https://www.geeksforgeeks.org/given-a-sequence-of-words-print-all-anagrams-together/

# Extras
