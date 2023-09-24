import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit

@timeit
def two_sum_naive(nums, target):
    left_index = 0
    right_index = 1
    
    for left_index in range(len(nums) - 1):
        for right_index in range(left_index + 1, len(nums)):
            total = nums[left_index] + nums[right_index]
            
            if total == target:
                return [left_index, right_index]

    return [left_index, right_index]

@timeit
def two_sum_difference_search(nums, target):
    left_index = 0
    right_index = 1
    difference_pairs = []
    twin_values = 0

    for index in range(len(nums)):
        difference_pairs.append(target - nums[index])
        
    for index in range(len(difference_pairs)):
        difference_pair = difference_pairs[index]
        
        if difference_pair == nums[index]:
            twin_values += 1
            if twin_values == 2:
                left_index = nums.index(difference_pair)
                nums.remove(difference_pair)
                right_index = nums.index(difference_pair) + 1
                return [left_index, right_index]
        elif difference_pair in nums:
            left_index = nums.index(difference_pair)
            right_index = nums.index(target - difference_pair)

            if left_index == right_index:
                nums.remove(difference_pair)
                right_index = nums.index(difference_pair) + 1
            
            return [left_index, right_index]

    return [left_index, right_index]

@timeit
def two_sum_map_search(nums, target):
    left_index = 0
    right_index = 1
    val_index_map = {}

    for left_index in range(len(nums)):
        left_pair = nums[left_index]
        right_pair = target - left_pair
        if right_pair in val_index_map:
            return [left_index, val_index_map[right_pair]]
        else:
            val_index_map[left_pair] = left_index

    return [left_index, right_index]


if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 9
    
    nums = [3, 2, 4]
    target = 6
        
    nums = [3, 3]
    target = 6
    
    nums = [3, -9, -9, 3]
    target = 6
        
    ans = two_sum_naive(nums, target)
    print(ans)

    ans = two_sum_difference_search(nums, target)
    print(ans)
    
    ans = two_sum_map_search(nums, target)
    print(ans)
    