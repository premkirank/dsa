import sys
import os
from functools import reduce

current_dir = os.path.dirname(os.path.realpath(__file__))
root_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(root_dir)

from utils.timeit import timeit


@timeit # 198 / 212 passed
def best_time_to_buy_and_sell_stock(prices):
    actual_prices = [price for price in prices]
    prices.sort()

    prices_index_map = {}
    max_profit = 0
    
    for index, price in enumerate(actual_prices):
        price = actual_prices[index]
        prices_index_map[price] = index

    for index in range(len(prices) - 1, -1, -1):
        max_price = prices[index]
        if prices_index_map[max_price] == 0:
            continue
        else:
            window = actual_prices[:prices_index_map[max_price]]
            # print(max_price, window)
            for min_price in window:
                if (max_price - min_price) > max_profit:
                    max_profit = max_price - min_price
            
    return max_profit

@timeit
def best_time_to_buy_and_sell_stock_greedy(prices):
    left_window_index = 0
    right_window_index = 1
    max_profit = 0
    
    while right_window_index < len(prices):
        left_window_price = prices[left_window_index]
        right_window_price = prices[right_window_index]

        if left_window_price > right_window_price:
            left_window_index += 1
        else:
            right_window_index += 1
            if right_window_price - left_window_price > max_profit:
                max_profit = right_window_price - left_window_price
               
    return max_profit


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    prices = [2, 1, 2, 0, 1]
    
    max_profit = best_time_to_buy_and_sell_stock_greedy(prices)
    print(max_profit)
    
    max_profit = best_time_to_buy_and_sell_stock(prices)
    print(max_profit)