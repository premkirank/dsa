# Problem

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Companies

# Level

Easy

# Status

Was not able to come up with optimal solution

# Tags

Arrays

# Approaches

- Naive Approach
  - Traverse the array in reverse order as we need to find max from last and min from before that to maximise profit
  - Find all pairs from reverse, subtract to find max profit
- Map, List Approach
  - Sort the array and keep it separately
  - Create a map of prices along with their indices
  - Traverse the sorted array in reverse order and for each price, see if they have any values left of them in actual array
  - If so, subtract them and look if any max profit is there
- Sliding Window Approach (best)

# Resources

https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/1735550/python-javascript-easy-solution-with-very-clear-explanation/

# Extras
