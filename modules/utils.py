import numpy as np
import pandas as pd
from IPython.display import display, HTML

# Calculate the product of cost_matrix and allocation_matrix
def calculate_total_cost(cost_matrix, allocation_matrix):
    total_cost = np.sum(cost_matrix * allocation_matrix)
    print(f"\nTotal Cost (Optimized): {total_cost} units\n")
    
def print_allocation(qty, i, j):
    print(f"Allocating {qty} units from Supplier {i+1} to Consumer {j+1}")

def update_supply_demand(result, supply, demand, i, j, qty):
    result[i, j] = qty
    supply[i] -= qty
    demand[j] -= qty
    
def style_dataframe(data):
    # Create a DataFrame starting from index 1
    df = pd.DataFrame(data, index=range(1, len(data) + 1), columns=range(1, len(data[0]) + 1))
    
    # Apply styling
    styled_df = df.style.background_gradient(cmap='Blues', axis=None)

    return styled_df