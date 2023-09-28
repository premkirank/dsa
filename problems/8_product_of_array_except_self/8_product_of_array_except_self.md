# Problem

https://leetcode.com/problems/product-of-array-except-self/

# Companies

# Level

Medium

# Status

Was not able to come up with optimal solution

# Tags

Arrays, Prefix Sum

# Approaches

- Naive Approach
  - Find the product of all numbers
  - Iterate and divide this number with the val at the index each time
- Prefix Suffix Product Approach
  - For each index, find left prefix product and right suffix product and return their product
  - Prefix product at each index is the product of the previous value, prefix product of that index
  - Suffix product at each index is the product of the next value, suffix product of that index

# Resources

- https://leetcode.com/problems/product-of-array-except-self/solutions/1597994/c-python-4-simple-solutions-w-explanation-prefix-suffix-product-o-1-space-approach/

# Extras
