#-------------------Problem------------------
# This problem was asked by Facebook.

# A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost while ensuring that no two neighboring houses are of the same color.

# Given an N by K matrix where the nth row and kth column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.

# ------------------Solution----------------
def build_houses(matrix):
    n = len(matrix)
    k = len(matrix[0])
    solution_matrix = [[0] * k]

    # Solution matrix: matrix[i][j] represents the minimum cost to build house i with color j.
    for r, row in enumerate(matrix):
        row_cost = []
        for c, val in enumerate(row):
            row_cost.append(min(solution_matrix[r][i] for i in range(k) if i != c) + val)
        solution_matrix.append(row_cost)
    return min(solution_matrix[-1])

# This runs in O(N K^2) time and O(N K) space. Can we do even better than this?

def build_houses(matrix):
    k = len(matrix[0])
    soln_row = [0] * k

    for r, row in enumerate(matrix):
        new_row = []
        for c, val in enumerate(row):
            new_row.append(min(soln_row[i] for i in range(k) if i != c) + val)
        soln_row = new_row
    return min(soln_row)


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


# Now the runtime is only O(N * K) and the space complexity is O(1) - constant, since we keep track of only three variables!