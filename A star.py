from queue import PriorityQueue

# Function to calculate the heuristic (Euclidean distance in this case)
def heuristic(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

# A* algorithm implementation
def a_star(graph, start, goal):
    # Priority queue to store (cost, node) with priority based on f = g + h
    open_set = PriorityQueue()
    open_set.put((0, start))  # (f_score, node)
    
    # Dictionaries to store the current shortest path to each node
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristic(start, goal)
    
    # Set of visited nodes
    visited = set()
    
    while not open_set.empty():
        current = open_set.get()[1]  # Get the node with the lowest f_score
        visited.add(current)
        
        # If the goal is reached, reconstruct the path
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        
        # Explore the neighbors of the current node
        for neighbor in graph[current]:
            if neighbor in visited:
                continue
            
            # Calculate the tentative g_score
            tentative_g_score = g_score[current] + graph[current][neighbor]
            
            if tentative_g_score < g_score[neighbor]:
                # This path to the neighbor is better, so record it
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                open_set.put((f_score[neighbor], neighbor))
    
    return None  # No path found

# Example graph as a dictionary of dictionaries (weighted graph)
graph = {
    (0, 0): {(0, 1): 1.5, (1, 0): 2},
    (0, 1): {(0, 0): 1.5, (1, 1): 2},
    (1, 0): {(0, 0): 2, (1, 1): 2.5},
    (1, 1): {(1, 0): 2.5, (0, 1): 2}
}

start = (0, 0)  # Starting node
goal = (1, 1)   # Goal node

# Run A* algorithm
path = a_star(graph, start, goal)

if path:
    print(f"Path found: {path}")
else:
    print("No path found.")
