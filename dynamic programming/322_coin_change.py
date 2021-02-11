import sys
from typing import List

system_max = sys.maxsize


def bottom_up_algorithm(coins: List[int], amount: int) -> int:
    max_value = amount + 1
    arr = [amount + 1] * max_value
    arr[0] = 0

    for local_target in range(1, amount + 1):
        for coin_value in coins:
            if local_target - coin_value >= 0:
                arr[local_target] = min(arr[local_target], arr[local_target - coin_value] + 1)
    return arr[-1] if arr[-1] != max_value else -1


def top_down_algorithm(coins: List[int], remainder: int, cache: List[int]) -> int:
    if remainder < 0:
        return -1

    if remainder == 0:
        return 0

    # this fact means that we've already solved this task in another recursion branch
    if cache[remainder] != 0:
        return cache[remainder]

    minimum = system_max
    for coin_cost in coins:
        res = top_down_algorithm(coins, remainder - coin_cost, cache)

        if res >= 0 and res < minimum:
            minimum = res + 1

    cache[remainder] = minimum if (minimum != system_max) else -1

    return cache[remainder]


def top_down_start(coins: List[int], amount: int) -> int:
    return top_down_algorithm(coins, amount, [0] * (amount + 1))


print(bottom_up_algorithm([1, 2, 5], 11))
