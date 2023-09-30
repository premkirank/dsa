# Problem

https://leetcode.com/problems/3sum/

# Companies

# Level

Medium

# Status

Was not able to come up with optimal solution

# Tags

Arrays, Two Pointers, Sorting

# Approaches

- Sort Approach
  - Sort the array
  - Keep a left_index and a right_index and iterate till left_index < right_index, left_window_index = left_index + 1, right_window_index = index of last val
  - Two Sum = (val of left_window_index) + (val at right_window_index)
  - Until left_window_index and right_window_index don't clash, if (target - val at left_index) < two_sum, increment left_window_index, else if > two_sum decrement right_window_index, else if == two_sum add the triplet and continue search 

# Resources

- https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

# Extras
