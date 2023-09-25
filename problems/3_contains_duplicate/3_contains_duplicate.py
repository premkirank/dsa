import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def contains_duplicate_map_search(nums):
    val_index_map = {}

    for index in range(len(nums)):
        if nums[index] in val_index_map:
            return True
        else:
            val_index_map[nums[index]] = index

    return False


if __name__ == "__main__":
    nums = [1, 2, 3 ,1]
            
    ans = contains_duplicate_map_search(nums)
    print(ans)
    