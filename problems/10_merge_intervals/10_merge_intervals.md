# Problem

https://leetcode.com/problems/merge-intervals/

# Companies

# Level

Medium

# Status

All tests passed but was not optimal approach

# Tags

Arrays, Sorting

# Approaches

- Sort Approach
  - Sort the array based on the first element value
  - Traverse the array and compare
    - if first_list_last_val > second_list_first_val && second_list_last_val, if so merge to [first_list_first_val, first_list_last_val]
    - else if first_list_last_val > second_list_first_val, if so merge to [first_list_first_val, second_list_last_val]

# Resources

- https://www.geeksforgeeks.org/merging-intervals/
- https://stackoverflow.com/questions/4174941/how-to-sort-a-list-of-lists-by-a-specific-index-of-the-inner-list
- https://stackoverflow.com/questions/27073596/what-is-the-cost-complexity-of-insert-in-list-at-some-location
- https://stackoverflow.com/questions/195625/what-is-the-time-complexity-of-popping-elements-from-list-in-python

# Extras
