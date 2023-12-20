import numpy as np  # Importing the NumPy library for numerical operations
from IPython.display import display
from .utils import calculate_total_cost, print_allocation, update_supply_demand

def calculate_penalties(cost_matrix, mask, iteration):
    # Initialize arrays to store penalties for each row and column
    row_penalties = np.zeros(cost_matrix.shape[0])
    col_penalties = np.zeros(cost_matrix.shape[1])

    for i in range(cost_matrix.shape[0]):
            unallocated_indices = np.where(~mask[i, :])[0]
            if len(unallocated_indices) > 1:
                sorted_costs = np.sort(cost_matrix[i, unallocated_indices])
                row_penalties[i] = sorted_costs[1] - sorted_costs[0]

    for j in range(cost_matrix.shape[1]):
        unallocated_indices = np.where(~mask[:, j])[0]
        if len(unallocated_indices) > 1:
            sorted_costs = np.sort(cost_matrix[unallocated_indices, j])
            col_penalties[j] = sorted_costs[1] - sorted_costs[0]
            
    print(f"\nIteration {iteration}:\n")
    print(f"Row Penalties: {row_penalties}")
    print(f"Column Penalties: {col_penalties}")
            
    # Return the calculated row and column penalties
    return row_penalties, col_penalties

def select_allocation_cell(row_penalties, col_penalties, mask, cost_matrix):
    if row_penalties.max() >= col_penalties.max():
        i = np.argmax(row_penalties)
        unmasked_col_indices = np.where(~mask[i, :])[0]
        j = unmasked_col_indices[np.argmin(cost_matrix[i, unmasked_col_indices])]
    else:
        j = np.argmax(col_penalties)
        unmasked_row_indices = np.where(~mask[:, j])[0]
        i = unmasked_row_indices[np.argmin(cost_matrix[unmasked_row_indices, j])]

    return i, j

def vogels_approximation_method(supply, demand, cost_matrix):
    # Copy the supply and demand arrays to avoid modifying the original data
    supply = supply.copy()
    demand = demand.copy()
    # Get the number of suppliers and consumers from the cost matrix dimensions
    num_suppliers, num_consumers = cost_matrix.shape
    # Initialize a mask to track allocated cells in the cost matrix
    mask = np.zeros((num_suppliers, num_consumers), dtype=bool)
    # Initialize a result matrix to store the allocation plan
    result = np.zeros((num_suppliers, num_consumers), dtype=int)
    iteration = 1

    # Continue the loop until all rows and columns have been assigned.
    while True:
        # Calculate penalties for the current state of the cost matrix
        row_penalties, col_penalties = calculate_penalties(cost_matrix, mask, iteration)
        # Find the maximum penalty across all rows and columns
        max_penalty = max(row_penalties.max(), col_penalties.max())

        #Displaying max penalty
        print(f"Max Penalty: {max_penalty}")
        
        # If no penalties are left, break the loop
        if max_penalty == 0:
            break

        i, j = select_allocation_cell(row_penalties, col_penalties, mask, cost_matrix)
        # Determine the quantity to allocate based on supply and demand
        qty = min(supply[i], demand[j])
        
        update_supply_demand(result, supply, demand, i, j, qty)
        mask[i, j] = True

        # Update the mask if the supply or demand of the selected cell becomes zero
        if qty > 0:
            print(f"Allocating {qty} units from Supplier {i+1} to Consumer {j+1}")
            
        iteration += 1
        
    # Return the final allocation plan
    return result
