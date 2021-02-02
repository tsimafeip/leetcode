from typing import List


def maxProfit(prices: List[int]) -> int:
    global_min, max_profit = prices[0], 0
    for price in prices[1:]:
        if price < global_min:
            global_min = price
        else:
            cur_profit = price - global_min
            if max_profit < cur_profit:
                max_profit = cur_profit
    return max_profit

