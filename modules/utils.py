import numpy as np

def calculate_total_cost(cost_matrix, allocation_matrix):
    total_cost = np.sum(cost_matrix * allocation_matrix)
    print(f"\nTotal Cost (Optimized): {total_cost} units\n")
    
def print_allocation(qty, i, j):
    print(f"Allocating {qty} units from Supplier {i+1} to Consumer {j+1}")

def update_supply_demand(result, supply, demand, i, j, qty):
    result[i, j] = qty
    supply[i] -= qty
    demand[j] -= qty