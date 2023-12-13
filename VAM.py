import numpy as np  # Importing the NumPy library for numerical operations

def calculate_penalties(cost_matrix, mask):
    # Initialize arrays to store penalties for each row and column
    row_penalties = np.zeros(cost_matrix.shape[0])
    col_penalties = np.zeros(cost_matrix.shape[1])

    # Calculate penalties for each row
    for i in range(cost_matrix.shape[0]):
        # Mask the current row based on the allocation status
        unmasked_row = np.ma.masked_array(cost_matrix[i, :], mask[i, :])
        # Check if there are at least two unallocated cells in the row
        if np.count_nonzero(~unmasked_row.mask) > 1:
            # Calculate the difference between the two smallest unallocated costs in the row
            row_penalties[i] = np.diff(np.sort(unmasked_row.compressed())[:2]).item()

    # Calculate penalties for each column
    for j in range(cost_matrix.shape[1]):
        # Mask the current column based on the allocation status
        unmasked_col = np.ma.masked_array(cost_matrix[:, j], mask[:, j])
        # Check if there are at least two unallocated cells in the column
        if np.count_nonzero(~unmasked_col.mask) > 1:
            # Calculate the difference between the two smallest unallocated costs in the column
            col_penalties[j] = np.diff(np.sort(unmasked_col.compressed())[:2]).item()

    # Return the calculated row and column penalties
    return row_penalties, col_penalties

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

    # Continue the allocation process as long as there is supply and demand
    while np.any(supply > 0) and np.any(demand > 0):
        # Calculate penalties for the current state of the cost matrix
        row_penalties, col_penalties = calculate_penalties(cost_matrix, mask)
        # Find the maximum penalty across all rows and columns
        max_penalty = max(row_penalties.max(), col_penalties.max())

        # If no penalties are left, break the loop
        if max_penalty == 0:
            break

        # Choose the row or column with the highest penalty for allocation
        if row_penalties.max() >= col_penalties.max():
            # Select the row with the highest penalty
            i = np.argmax(row_penalties)
            # Find indices of unallocated cells in the selected row
            unmasked_col_indices = np.where(~mask[i, :])[0]
            # Choose the cell with the lowest cost in the selected row
            j = unmasked_col_indices[np.argmin(cost_matrix[i, unmasked_col_indices])]
        else:
            # Select the column with the highest penalty
            j = np.argmax(col_penalties)
            # Find indices of unallocated cells in the selected column
            unmasked_row_indices = np.where(~mask[:, j])[0]
            # Choose the cell with the lowest cost in the selected column
            i = unmasked_row_indices[np.argmin(cost_matrix[unmasked_row_indices, j])]

        # Determine the quantity to allocate based on supply and demand
        qty = min(supply[i], demand[j])
        # Allocate the quantity to the selected cell
        result[i, j] = qty
        # Update the supply and demand after allocation
        supply[i] -= qty
        demand[j] -= qty

        # Update the mask if the supply or demand of the selected cell becomes zero
        if supply[i] == 0:
            mask[i, :] = True
        if demand[j] == 0:
            mask[:, j] = True

        # Print the allocation details
        print(f"Allocating {qty} units from Supplier {i+1} to Consumer {j+1}")

    # Return the final allocation plan
    return result

# Define the supply, demand, and cost matrix for the problem
supply = np.array([22, 25, 10])
demand = np.array([8, 8, 12, 29])
cost_matrix = np.array([
    [10, 19, 5, 7],
    [13, 2, 7, 8],
    [15, 18, 6, 14]
])

# Solve the transportation problem using Vogel's Approximation Method
solution = vogels_approximation_method(supply, demand, cost_matrix)
# Print the final transportation plan
print("Transportation Plan:")
print(solution)
