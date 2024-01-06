import sys
import os
from functools import reduce
from operator import itemgetter

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def max_product_subarray_simple(nums):
    max_subarray_product = nums[0]
    imax = imin = max_subarray_product

    for index in range(1, len(nums)):
        if nums[index] < 0:
            imax, imin = imin, imax
        
        imax = max(nums[index], imax * nums[index])
        imin = min(nums[index], imin * nums[index])
        
        print(index, imax, imin)
        max_subarray_product = max(max_subarray_product, imax)

    return max_subarray_product

@timeit
def max_product_subarray(nums): 
    max_ending_here = nums[0]
    min_ending_here = nums[0] 
    max_so_far = nums[0]
 
    for index in range(1, len(nums)):
        temp = max(max(nums[index], nums[index] * max_ending_here), nums[index] * min_ending_here)
        min_ending_here = min(min(nums[index], nums[index] * max_ending_here), nums[index] * min_ending_here)
        max_ending_here = temp
        max_so_far = max(max_so_far, max_ending_here)
        
        print(index, max_ending_here, min_ending_here)
 
    return max_so_far


if __name__ == "__main__":
    nums = [-2, 0, -1]
    nums = [-4, -3]
    nums = [2, -5, -2, -4, 3]
    nums = [-2, 3, -4]   
    nums = [0, 2]
    nums = [1, 0, -1, 2, 3, -5, -2]
    nums = [2, 3, -2, 4]

    output = max_product_subarray(nums)
    print(output)
    