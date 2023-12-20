# Vogel Approximation Method
![vogel_result](https://github.com/faridnec/vogels-approx-method/blob/main/img/output.png?raw=true)
### Overview
The example transportation problem for the output above is as follows
```python
supply = np.array([22, 25, 10])
demand = np.array([8, 8, 12, 29])
cost_matrix = np.array([
    [10, 19, 5, 7],
    [13, 2, 7, 8],
    [15, 18, 6, 14]
])
```
### Introduction
Vogel's Approximation Method (VAM) is an algorithm used for solving transportation problems in linear programming. A transportation problem involves minimizing the cost of transporting goods from multiple suppliers to multiple consumers. Vogel's method provides an iterative approach to find an initial feasible solution, which can then be improved using other optimization techniques.

Reference:  
BYJU's. (n.d.). Vogel's Approximation Method. BYJU's. https://byjus.com/maths/vogels-approximation-method/

Here is the project structure:
```plaintext
project/
|-- img/
|-- modules/
|   |-- vam.py      # VAM algorithm
|   |-- utils.py    # utility outside VAM 
|-- main_script.py  # running VAM
|-- Readme.md
```

### Installation
This project using numpy library assuming you have got pip on your system. Install numpy on your repository
```bash
pip install numpy
```

### Output
Run main_script.py
```bash
python main_script.py
```
Here is the output from previous example:
```plaintext
Allocating 8 units from Supplier 2 to Consumer 2
Allocating 10 units from Supplier 3 to Consumer 3
Allocating 8 units from Supplier 1 to Consumer 1
Allocating 2 units from Supplier 1 to Consumer 3
Allocating 12 units from Supplier 1 to Consumer 4
Allocating 17 units from Supplier 2 to Consumer 4

Total Cost (Optimized): 386 units

Transportation Plan:
[[ 8  0  2 12]
 [ 0  8  0 17]
 [ 0  0 10  0]]
```
