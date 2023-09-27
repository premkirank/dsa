import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def maximum_subarray_naive(nums):
    index_sum = {}
    max_subarray_sum = 0    
    
    for index, val in enumerate(nums):
        if index == 0:
            index_sum[index] = val
            max_subarray_sum = val
        else:
            index_sum[index] = index_sum[index - 1] + val
            left_index = 0
            while left_index < index:
                cur_max_subarray_sum = max(val, index_sum[index], index_sum[index] - index_sum[left_index])        
                if cur_max_subarray_sum > max_subarray_sum:
                    max_subarray_sum = cur_max_subarray_sum

                left_index += 1

    return max_subarray_sum

@timeit
def maximum_subarray_dp(nums):
    index_sum = {}
    max_subarray_sum = 0
    max_contiguous_sum_per_index = {}
    
    for index, val in enumerate(nums):
        if index == 0:
            index_sum[index] = val
            max_subarray_sum = val
            max_contiguous_sum_per_index[0] = val
        else:
            index_sum[index] = index_sum[index - 1] + val
            max_contiguous_sum_per_index[index] = max(val, index_sum[index], max_contiguous_sum_per_index[index - 1] + val)        
            if max_contiguous_sum_per_index[index] > max_subarray_sum:
                max_subarray_sum = max_contiguous_sum_per_index[index]

    return max_subarray_sum


if __name__ == "__main__":
    nums = [1]
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [5, 4, -1, 7, 8]    
    
    ans = maximum_subarray_naive(nums)
    print(ans)

    ans = maximum_subarray_dp(nums)
    print(ans)
