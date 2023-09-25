# Problem

- https://leetcode.com/problems/subarray-product-less-than-k/

# Companies

1. [ServiceNow](https://www.servicenow.com/) - Sep 23 2023 - Hackerrank Online Test (90 min, Question 1 of 2)

# Level

Medium

# Status

Was not able to come up with optimal solution

# Tags

Arrays, Sliding Window

# Approaches

- Naive Approach
  - Forming all contiguous subarrays
  - Product of all values in subarray and filtering based on product < k
- DP Approach
  - DFS iteration
  - Product of current subarray is product of previous subarray * last value in current subarray
  - Stopping further search for an index if product > k
  - Storing computed product values in a Map for lookup e.g ```{"[2,3]": 6```
- Sliding Window Approach (best)

# Resources

- https://youtu.be/NbgRSeV_ypU?si=Lzq5n3Z0KSSmvBoM

# Extras

- Instead of count of valid subarrays, need the actual subarrays to be returned
