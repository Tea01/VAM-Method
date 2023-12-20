import numpy as np
from modules.vam import vogels_approximation_method
from modules.utils import calculate_total_cost, print_allocation, update_supply_demand

# EXAMPLE 1
supply = np.array([22, 25, 10])
demand = np.array([8, 8, 12, 29])
cost_matrix = np.array([
    [10, 19, 5, 7],
    [13, 2, 7, 8],
    [15, 18, 6, 14]
])

# Example 2
# supply = np.array([300, 400, 500])
# demand = np.array([250, 350, 400, 200])
# cost_matrix = np.array([
#     [3, 1, 7, 4],
#     [2, 6, 5, 9],
#     [8, 3, 3, 2]
# ])

def main():
    # Solve the transportation problem using Vogel's Approximation Method
    solution = vogels_approximation_method(supply, demand, cost_matrix)

    # Print the final transportation plan
    calculate_total_cost(cost_matrix, solution)
    
    # Print the final transportation plan
    print("Transportation Plan:")
    print(solution)

if __name__ == "__main__":
    main()
