# Problem

https://leetcode.com/problems/valid-parentheses/

# Companies

# Level

Easy

# Status

Was able to come up with optimal approach

# Tags

String, Stack

# Approaches

- Map Approach
  - Create map associating opening brackets with +ve unique values and closing ones with complementary -ve values
  - Iterate on string and add values to stack if > 0
  - If < 0 check if stack is empty, if so invalid else pop value and check if it is complement of the popped value else invalid
  - If stack is not empty in the end, invalid

# Resources

- https://leetcode.com/problems/valid-parentheses/solutions/3399077/easy-solutions-in-java-python-and-c-look-at-once-with-exaplanation/

# Extras
