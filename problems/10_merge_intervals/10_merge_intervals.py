import sys
import os
from functools import reduce
from operator import itemgetter

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit
def merge_intervals_sort(intervals):
    intervals = sorted(intervals, key=itemgetter(0))

    merge_done = True
    
    while merge_done:
        merge_done = False

        for index in range(len(intervals) - 1):
            iv_left_val, iv_right_val = intervals[index]
            niv_left_val, niv_right_val = intervals[index + 1]
            if iv_right_val >= niv_left_val:
                intervals.pop(index)
                intervals.pop(index)
                if iv_right_val >= niv_right_val:
                    intervals.insert(index, [iv_left_val, iv_right_val])
                else:
                    intervals.insert(index, [iv_left_val, niv_right_val])
                merge_done = True
                break
        
    return intervals

@timeit
def merge_intervals_sort_and_optimized(intervals):
    intervals.sort(key=lambda x: x[0])
    
    last_output_index = 0

    for index in range(1, len(intervals)):
        if (intervals[last_output_index][1] >= intervals[index][0]):
            intervals[last_output_index][1] = max(intervals[last_output_index][1], intervals[index][1])
        else:
            last_output_index = last_output_index + 1
            intervals[last_output_index] = intervals[index]
        
        print(intervals)
        
    return intervals[:last_output_index + 1]


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    intervals = [[1, 4], [4, 5]]
    intervals = [[0, 4], [1, 2]]
    intervals = [[1, 4], [0, 4]]
    intervals = [[4, 5], [1, 4],[0, 1]]
    intervals = [[1, 3], [2, 4], [2, 6], [8, 10], [15, 18]]
    
    output = merge_intervals_sort(intervals)
    print(output)
    
    output = merge_intervals_sort_and_optimized(intervals)
    print(output)
