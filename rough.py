from collections import deque

goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def find_blank(state):
    for i, row in enumerate(state):
        if 0 in row:
            return i, row.index(0)

def generate_moves(state):
    x, y = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            yield new_state

def bfs(initial_state):
    queue = deque([initial_state])
    visited = {tuple(map(tuple, initial_state)): None}
    
    while queue:
        state = queue.popleft()
        if state == goal_state:
            path = []
            while state:
                path.append(state)
                state = visited[tuple(map(tuple, state))]
            return path[::-1]
        
        for neighbor in generate_moves(state):
            neighbor_tuple = tuple(map(tuple, neighbor))
            if neighbor_tuple not in visited:
                visited[neighbor_tuple] = state
                queue.append(neighbor)
    return None

def main():
    initial_state = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]
    solution = bfs(initial_state)

    if solution:
        for step, state in enumerate(solution):
            print(f"Step {step}:")
            for row in state:
                print(' '.join(str(n) if n != 0 else ' ' for n in row))
            print()
    else:
        print("No solution found.")

if __name__== "_main_":
    main()