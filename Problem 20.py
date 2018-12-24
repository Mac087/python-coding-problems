# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

from math import inf

def build_houses(matrix):
    lowest_cost, lowest_cost_index = 0, -1
    second_lowest_cost = 0

    for r, row in enumerate(matrix):
        new_lowest_cost, new_lowest_cost_index = inf, -1
        new_second_lowest_cost = inf
        for c, val in enumerate(row):
            prev_lowest_cost = second_lowest_cost if c == lowest_cost_index else lowest_cost
            cost = prev_lowest_cost + val
            if cost < new_lowest_cost:
                new_second_lowest_cost = new_lowest_cost
                new_lowest_cost, new_lowest_cost_index = cost, c
            elif cost < new_second_lowest_cost:
                new_second_lowest_cost = cost
        lowest_cost = new_lowest_cost
        lowest_cost_index = new_lowest_cost_index
        second_lowest_cost = new_second_lowest_cost

    return lowest_cost