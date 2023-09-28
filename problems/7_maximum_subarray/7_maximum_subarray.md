# Problem

https://leetcode.com/problems/maximum-subarray/

# Companies

# Level

Medium

# Status

All tests passed but was not optimal approach

# Tags

Arrays, DP, Divide & Conquer

# Approaches

- Naive Approach
  - For each index, store the sum till that index
  - While iterating on each index, find max of cur value, sum till that index, sum of values removing leftmost individual element each time
- DP Approach
  - For each index, store the max possible contiguous max array sum till that index
  - Find max of cur_val, cur_val + prev_index max contiguous sum in each iteration

# Resources

- https://leetcode.com/problems/maximum-subarray/solutions/1595195/c-python-7-simple-solutions-w-explanation-brute-force-dp-kadane-divide-conquer/

# Extras
