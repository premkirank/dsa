import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit

def sub_array_product(sub_array):
    return reduce(lambda x, y: x * y , sub_array)

def sub_array_product_dp(prev_sub_array_product, last_val_sub_array):
    return prev_sub_array_product * last_val_sub_array

@timeit
def count_sub_arrays_naive(array, size, k):
    max_subarray_len = size
    sub_arrays_count = 0

    for left_index in range(0, max_subarray_len): # iterate on index
        for subarray_len in range(1, max_subarray_len + 1): # to limit sub_array size
            right_index = left_index + subarray_len
            if right_index <= max_subarray_len:
                sub_array = array[left_index:right_index]
                # print(sub_array)
                if sub_array_product(sub_array) < k:
                    sub_arrays_count += 1
                else:
                    break
                
    return sub_arrays_count

@timeit
def count_sub_arrays_dp(array, size, k):
    max_subarray_len = size
    sub_arrays_count = 0

    for left_index in range(0, max_subarray_len): # iterate on index
        prev_sub_array_product = 1
        for subarray_len in range(1, max_subarray_len + 1): # to limit sub_array size
            right_index = left_index + subarray_len
            if right_index <= max_subarray_len:
                sub_array = array[left_index:right_index]
                last_val_sub_array = sub_array[-1]

                # print(sub_array)

                if subarray_len == 1:
                    prev_sub_array_product = sub_array_product_dp(prev_sub_array_product, last_val_sub_array)
                elif subarray_len > 1:
                    prev_sub_array_product = sub_array_product_dp(prev_sub_array_product, last_val_sub_array)

                if prev_sub_array_product < k:
                    sub_arrays_count += 1
                else:
                    break
                
    return sub_arrays_count

@timeit
def count_sub_arrays_sliding_window(array, size, k):
    max_sub_array_len = size
    sub_arrays_count = 0
    
    left_window_index = 0
    left_window_index_updated = False
    right_window_index = 0
    product = 1

    while right_window_index < max_sub_array_len:
        if not left_window_index_updated:
            product *= array[right_window_index]

        if product < k:
            sub_arrays_count += (right_window_index - left_window_index) + 1
            right_window_index += 1
            left_window_index_updated = False
            # print(product, left_window_index, right_window_index, array[left_window_index: right_window_index], sub_arrays_count)
        elif left_window_index == max_sub_array_len:
            if array[left_window_index] < k:
                sub_arrays_count += 1
            right_window_index += 1
        elif left_window_index == right_window_index:
            right_window_index += 1
            left_window_index += 1            
            product = 1
            left_window_index_updated = False
        else:
            product = int(product / array[left_window_index])
            left_window_index += 1
            left_window_index_updated = True
            # print(product, left_window_index, right_window_index)
                       
    return sub_arrays_count        

if __name__ == "__main__":
    array = [1, 11, 2, 3, 15]
    k = 10
        
    array = [10, 5, 2, 6]
    k = 100
    
    array = [1, 1, 1]
    k = 1
    
    size = len(array)
    count = count_sub_arrays_naive(array, size, k)
    print(count)
    count = count_sub_arrays_dp(array, size, k)
    print(count)
    count = count_sub_arrays_sliding_window(array, size, k)
    print(count)
