import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def three_sum(nums):
    valid_triplets = []
    left_index = 0
    right_index = len(nums) - 1
    
    nums.sort()
    
    while left_index < right_index:
        left_window_index = left_index + 1
        right_window_index = right_index
        
        while left_window_index < right_window_index:
            triplet = [nums[left_index]]
            target_sum = 0 - nums[left_index]
            
            two_sum = nums[left_window_index] + nums[right_window_index]
            # print(left_index, two_sum, target_sum, left_window_index + 1, right_window_index)
            
            if two_sum == target_sum:
                triplet.append(nums[left_window_index])
                triplet.append(nums[right_window_index])
                if triplet not in valid_triplets:
                    valid_triplets.append(triplet)
                left_window_index += 1
            elif two_sum < target_sum:
                left_window_index += 1
            else:
                right_window_index -= 1
                                
        left_index += 1

    return valid_triplets

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    nums = [-1, 1, 2, -1, -4]
    nums = [-1, -2, 1, 2, 0, 0, -4]
    nums = [0, 0, 0, 0]
    nums = [-2, 0, 1, 1, 2]
    
    valid_triplets = three_sum(nums)
    print(valid_triplets)
