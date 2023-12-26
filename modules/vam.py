import numpy as np  # Importing the NumPy library for numerical operations
from IPython.display import display  # Importing display from IPython for output display
from .utils import calculate_total_cost, print_allocation, update_supply_demand  # Importing utility functions from a local module

def calculate_penalties(cost_matrix, mask, iteration):
    # Initialize arrays to store penalties for each row and column of the cost matrix
    row_penalties = np.zeros(cost_matrix.shape[0])
    col_penalties = np.zeros(cost_matrix.shape[1])

    # Calculate penalties for each row
    for i in range(cost_matrix.shape[0]):
            unallocated_indices = np.where(~mask[i, :])[0]  # Find indices of unallocated cells in the row
            if len(unallocated_indices) > 1:  # Check if there are more than one unallocated cells
                sorted_costs = np.sort(cost_matrix[i, unallocated_indices])  # Sort the costs of these cells
                row_penalties[i] = sorted_costs[1] - sorted_costs[0]  # Calculate penalty as difference between the two smallest costs

    # Calculate penalties for each column
    for j in range(cost_matrix.shape[1]):
        unallocated_indices = np.where(~mask[:, j])[0]  # Find indices of unallocated cells in the column
        if len(unallocated_indices) > 1:  # Check if there are more than one unallocated cells
            sorted_costs = np.sort(cost_matrix[unallocated_indices, j])  # Sort the costs of these cells
            col_penalties[j] = sorted_costs[1] - sorted_costs[0]  # Calculate penalty as difference between the two smallest costs
            
    # Print current iteration and penalties for debugging
    print(f"\nIteration {iteration}:\n")
    print(f"Row Penalties: {row_penalties}")
    print(f"Column Penalties: {col_penalties}")
            
    # Return the calculated row and column penalties
    return row_penalties, col_penalties

def select_allocation_cell(row_penalties, col_penalties, mask, cost_matrix):
    # Decide whether to allocate based on row or column penalty
    if row_penalties.max() >= col_penalties.max():  # If max row penalty is greater than or equal to max column penalty
        i = np.argmax(row_penalties)  # Get the index of the row with max penalty
        unmasked_col_indices = np.where(~mask[i, :])[0]  # Find unallocated columns in this row
        j = unmasked_col_indices[np.argmin(cost_matrix[i, unmasked_col_indices])]  # Select the column with minimum cost
    else:
        j = np.argmax(col_penalties)  # Get the index of the column with max penalty
        unmasked_row_indices = np.where(~mask[:, j])[0]  # Find unallocated rows in this column
        i = unmasked_row_indices[np.argmin(cost_matrix[unmasked_row_indices, j])]  # Select the row with minimum cost

    # Return the indices of the selected cell
    return i, j

def vogels_approximation_method(supply, demand, cost_matrix):
    # Vogel's Approximation Method for solving transportation problem
    supply = supply.copy()  # Create a copy of the supply array to avoid modifying the original
    demand = demand.copy()  # Create a copy of the demand array to avoid modifying the original
    num_suppliers, num_consumers = cost_matrix.shape  # Get the number of suppliers and consumers
    mask = np.zeros((num_suppliers, num_consumers), dtype=bool)  # Initialize a mask to track allocated cells
    result = np.zeros((num_suppliers, num_consumers), dtype=int)  # Initialize a matrix to store the allocation results
    iteration = 1  # Initialize iteration counter

    # Main loop for allocation
    while True:
        row_penalties, col_penalties = calculate_penalties(cost_matrix, mask, iteration)  # Calculate penalties
        max_penalty = max(row_penalties.max(), col_penalties.max())  # Find the maximum penalty

        # Print the maximum penalty for debugging
        print(f"Max Penalty: {max_penalty}")
        
        if max_penalty == 0:  # If there are no penalties, break the loop
            break

        i, j = select_allocation_cell(row_penalties, col_penalties, mask, cost_matrix)  # Select a cell for allocation
        qty = min(supply[i], demand[j])  # Determine the quantity to allocate based on supply and demand
        
        update_supply_demand(result, supply, demand, i, j, qty)  # Update supply, demand, and allocation
        mask[i, j] = True  # Mark the allocated cell in the mask

        if qty > 0:  # Print allocation details if any quantity is allocated
            print(f"Allocating {qty} units from Supplier {i+1} to Consumer {j+1}")
            
        iteration += 1  # Increment iteration counter
        
    # Return the final allocation plan
    return result
