# Backtracking algorithm to solve map coloring CSP

# Function to check if current color assignment is valid (no adjacent regions share the same color)
def is_valid(node, color, assignment, neighbors):
    for neighbor in neighbors[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking algorithm for map coloring
def backtrack(assignment, nodes, colors, neighbors):
    # If all nodes have been assigned a color, return the assignment
    if len(assignment) == len(nodes):
        return assignment
    
    # Select an unassigned node
    unassigned_nodes = [node for node in nodes if node not in assignment]
    node = unassigned_nodes[0]
    
    # Try each color for the selected node
    for color in colors:
        if is_valid(node, color, assignment, neighbors):
            assignment[node] = color  # Assign color
            result = backtrack(assignment, nodes, colors, neighbors)  # Recursively assign colors to other nodes
            if result:
                return result
            assignment.pop(node)  # Backtrack if not successful
    
    return None  # No valid assignment found

# Example usage with a sample map of countries
def map_coloring_csp(nodes, colors, neighbors):
    assignment = {}  # Initial empty assignment
    return backtrack(assignment, nodes, colors, neighbors)

# Define the map (nodes and edges)
nodes = ['Western Australia', 'Northern Territory', 'South Australia', 
         'Queensland', 'New South Wales', 'Victoria', 'Tasmania']

neighbors = {
    'Western Australia': ['Northern Territory', 'South Australia'],
    'Northern Territory': ['Western Australia', 'South Australia', 'Queensland'],
    'South Australia': ['Western Australia', 'Northern Territory', 'Queensland', 'New South Wales', 'Victoria'],
    'Queensland': ['Northern Territory', 'South Australia', 'New South Wales'],
    'New South Wales': ['Queensland', 'South Australia', 'Victoria'],
    'Victoria': ['South Australia', 'New South Wales'],
    'Tasmania': []  # Tasmania doesn't share a border with any other region
}

# Colors available
colors = ['Red', 'Green', 'Blue']

# Solve the CSP
solution = map_coloring_csp(nodes, colors, neighbors)

if solution:
    print("Solution found:")
    for node, color in solution.items():
        print(f"{node}: {color}")
else:
    print("No solution found.")
