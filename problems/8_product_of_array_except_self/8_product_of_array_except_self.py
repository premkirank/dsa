import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def product_of_array_except_self_prefix_suffix_products_2_loops(nums):
    products_except_self = [1] * len(nums)
    left_products_except_self = [1] * len(nums)
    right_products_except_self = [1] * len(nums)
    
    for index, _ in enumerate(nums):
        if index == 0:
            left_products_except_self[index] = 1
            right_products_except_self[len(nums) - index - 1] = 1
        else:
            left_products_except_self[index] = left_products_except_self[index - 1] * nums[index - 1]
            right_products_except_self[len(nums) - index - 1] = right_products_except_self[len(nums) - index] * nums[len(nums) - index]
            
    for index, _ in enumerate(nums):
        products_except_self[index] = left_products_except_self[index] * right_products_except_self[index]

    return products_except_self

@timeit
def product_of_array_except_self_prefix_suffix_products_1_loop(nums):
    products_except_self = [1] * len(nums)
    prefix_product = suffix_product = 1
    
    for index, _ in enumerate(nums):
        # print(index, products_except_self, prefix_product, suffix_product)

        products_except_self[index] *= prefix_product
        prefix_product *= nums[index]
        products_except_self[len(nums) - index - 1] *= suffix_product
        suffix_product *= nums[len(nums) - index - 1]
        
        # print(index, products_except_self, prefix_product, suffix_product)

    return products_except_self


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]  
        
    ans = product_of_array_except_self_prefix_suffix_products_2_loops(nums)
    print(ans)

    ans = product_of_array_except_self_prefix_suffix_products_1_loop(nums)
    print(ans)