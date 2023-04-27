# EXERCISE 3. You are given an array prices where prices[i] is the price of agiven stock on the i-th day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
# Return the maximum profit you can achieve from this transaction and indexes of days (purchase, sell). If you
# cannot achieve any profit, return 0.
# Example: price_list = [10, 2, 12, 5, 1, 7, 3, 2, 9, 5]
# -> profit = 10, day_start = 2, day_sell = 3

def max_profit(prices):
    profit = 0
    for i in range(len(prices) - 1):
        for j in range(i + 1, len(prices) - 1):
            current_profit = prices[j] - prices[i]
            if current_profit > profit:
                profit = current_profit
    return profit


print(max_profit([10, 2, 12, 5, 1, 7, 3, 2, 9, 5]))

# EXERCISE 4. You are climbing a staircase. It takes n steps to reach the top. Each time  you can either climb
# 1 or 2 steps. In how many distinct ways can you climb to the top?
# Example:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def count_ways(n):
    p1 = 1
    p2 = 1
    for i in range(2, n + 1):
        c = p1 + p2
        p2 = p1
        p1 = c
    return p1


print(count_ways(3))
